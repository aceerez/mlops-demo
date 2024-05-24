# mlops-demo
# MLOps Assignment Documentation
## Objective
Deploy a pre-trained machine learning model as a RESTful API service and set up basic monitoring and logging. This includes:
1. Model Deployment
2.	Containerization
3.	Logging Setup
4.	Monitoring Setup
## Prerequisites
* Docker: Ensure Docker is installed on your system.
* Docker Compose: Ensure Docker Compose is installed on your system
## Steps to Build and Run the Application

1. clone the porject to your server
   
   ``` git clone https://github.com/aceerez/mlops-demo.git```

2. run the script start.sh to start the FlaskApi App and the Monitor tool 
   
```bash start.sh ```

## Access the Services of the App
When the app finishes loading, the addresses of the services will be displayed.
## Using the API
 Use the API address to query the model. Below is an example of how to test the API using curl.
 
 ``` curl -X POST -F 'file=@path_to_your_image.jpg' http://<SERVER_IP>:5000/predict ```
 
Replace path_to_your_image.jpg with the path to the image you want to use for prediction.

## Using the Monitoring Tool
Use the Grafana address to enter the monitoring tool to monitor the app.
1. Enter the address from your local browser (needs to be on the same VLAN as the server or have access to it).
2. Enter the login credentials:
```
Username: admin
Password: admin
```
4. On the first login, you will be prompted to change your password.
5. Each panel has a name indicating the logs it monitors.

## closing the App
to close the app, run the stop-app.sh
```bash stop-app.sh```

## Testing the App
inside the test_app folder, run the test.py script 

``` python3 test.py ```

this script test the api and create logs for Grafana to monitor. 
