import os
import requests
import time
import json

# URL of the Flask API endpoint
url = "http://localhost:5000/predict"

# Path to the folder containing image files
images_folder = "images"  # Change this to your actual folder name

# Delay between requests in seconds
delay = 1
# Number of Repeted requests 
repeat_count = 10

def send_valid_request(image_path, request_num):
    with open(image_path, 'rb') as img:
        files = {'file': img}
        response = requests.post(url, files=files)
        print(f"Valid Request {request_num} - Status Code: {response.status_code}")
        try:
            print(f"Response: {response.json()}")
        except json.JSONDecodeError:
            print("Failed to decode JSON response")
        print()

def send_missing_file_request(request_num):
    response = requests.post(url)
    print(f"Missing File Request {request_num} - Status Code: {response.status_code}")
    try:
        print(f"Response: {response.json()}")
    except json.JSONDecodeError:
        print("Failed to decode JSON response")
    print()

def send_invalid_file_request(image_path, request_num):
    with open(image_path, 'rb') as file:
        files = {'file': file}
        response = requests.post(url, files=files)
        print(f"Invalid File Request {request_num} - Status Code: {response.status_code}")
        try:
            print(f"Response: {response.json()}")
        except json.JSONDecodeError:
            print("Failed to decode JSON response")
        print()

def main():
    # Send valid requests for all images in the folder
    valid_images = [f for f in os.listdir(images_folder) if os.path.isfile(os.path.join(images_folder, f))]
    for _ in range(repeat_count):
        for i, image in enumerate(valid_images, start=1):
            image_path = os.path.join(images_folder, image)
            send_valid_request(image_path, i)
            time.sleep(delay)

    # Send missing file requests
    for i in range(1, 4):  # Sending 3 missing file requests
        send_missing_file_request(i)
        time.sleep(delay)

    # Send invalid file requests
    for i in range(1, 4):  # Sending 3 invalid file requests
        send_invalid_file_request("invalid_file.txt", i)
        time.sleep(delay)

if __name__ == "__main__":
    main()
