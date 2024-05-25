# mlops-demo
# MLOps Assignment Documentation
## Objective
Deploy a pre-trained machine learning model as a RESTful API service and set up basic monitoring and logging. This includes:
1. Model Deployment
2.	Containerization
3.	Logging Setup
4.	Monitoring Setup
## Prerequisites
* Linux system with bash (e.g., Ubuntu)
* Docker: Ensure Docker is installed on your system.
* Docker Compose: Ensure Docker Compose is installed on your system

## Steps to Build and Run the Application

1. clone the porject to your server
   
   ``` git clone https://github.com/aceerez/mlops-demo.git```

2. Enter the project directory and run the script start.sh to start the FlaskApi App and the Monitor tool 
   
```bash start.sh ```

## Access the Services of the App
When the app finishes loading, the addresses of the services will be displayed.
## Using the API
 Use the API address to query the model. Below is an example of how to test the API using curl.
 
 ``` curl -X POST -F 'file=@path_to_your_image.jpg' http://<SERVER_IP>:5000/predict ```
 
Replace path_to_your_image.jpg with the path to the image you want to use for prediction.

## Using the Monitoring Tool
Use the Grafana address to enter the monitoring tool to monitor the app.

 ### 1. Access Grafana
   * Open your local browser and enter the Grafana address (ensure your device is on the same VLAN as the server or has access to it).
### 2. Login
* Enter the login credentials:
```
Username: admin
Password: admin
```
* On the first login, you will be prompted to change your password.
### 3. Navigate to the Dashboard:
* Press the Dashboard button from the left side menu.
* Under Name, press MLOps. This will take you to the App dashboard.
* After the first login. the link provided in the app will take you to dashboard directly 
### 4. Viewing Logs and Metrics:
* Each panel on the dashboard has a name indicating the logs or metrics it monitors.

## closing the App
to close the app, run the stop-app.sh
```bash stop-app.sh```

## Testing the App
inside the for_test folder, run the test.py script 

``` python3 test.py ```

this script test the api and create logs for Grafana to monitor. 
