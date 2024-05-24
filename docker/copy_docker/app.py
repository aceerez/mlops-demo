from flask import Flask, request, jsonify
import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import io
import logging
from prometheus_client import start_http_server, Summary, Counter

# Initialize Flask application
app = Flask(__name__)

# Load the model
model = models.resnet18(weights=models.ResNet18_Weights.IMAGENET1K_V1)
model.eval()

# Define image transformations
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Load ImageNet class labels
with open('imagenet_classes.txt') as f:
    labels = [line.strip() for line in f.readlines()]

# Setup basic logging to log everything
logging.basicConfig(filename='res18api.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Start Prometheus metrics server
start_http_server(8000)

# Create metrics
REQUEST_COUNT = Counter('request_count_total', 'Total number of requests')
REQUEST_LATENCY = Summary('request_latency_seconds', 'Request latency in seconds')
REQUEST_ERRORS = Counter('request_errors_total', 'Total number of request errors')

def transform_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes))
    return transform(image).unsqueeze(0)

def get_prediction(image_bytes):
    tensor = transform_image(image_bytes)
    outputs = model.forward(tensor)
    _, predicted_idx = outputs.max(1)
    predicted_idx = predicted_idx.item()
    predicted_label = labels[predicted_idx]
    return predicted_idx, predicted_label

@app.before_request
def log_request_info():
    logging.info(f"Incoming request: {request.method} {request.url}")
    logging.info(f"Request headers: {request.headers}")
    if request.data:
        logging.info(f"Request body: {request.get_data()}")

@app.after_request
def log_response_info(response):
    logging.info(f"Response status: {response.status}")
    logging.info(f"Response headers: {response.headers}")
    logging.info(f"Response body: {response.get_data(as_text=True)}")
    return response

@app.route('/predict', methods=['POST'])
@REQUEST_LATENCY.time()
def predict():
    REQUEST_COUNT.inc()
    if 'file' not in request.files:
        logging.error("No file provided")
        REQUEST_ERRORS.inc()
        return jsonify({'error': 'no file provided'}), 400

    file = request.files['file']
    img_bytes = file.read()
    logging.info("Received file for prediction")
    try:
        predicted_idx, predicted_label = get_prediction(img_bytes)
        logging.info(f"Prediction result: index={predicted_idx}, label={predicted_label}")
        return jsonify({'prediction_index': predicted_idx, 'prediction_label': predicted_label})
    except Exception as e:
        logging.error(f"Error during prediction: {str(e)}")
        REQUEST_ERRORS.inc()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
