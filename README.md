# Webservice to display real-time raining data for a particular location.

### This application is developed in Python3 programming language and using Flask, uWSGI as local web server. 
Ngnix has been used as a production webserver to deal with clients requests. 

<p>This app will fetch real-time weather info from https://api.data.gov.sg/v1/environment/rainfall and display raining data for a given location.
</p>

<p> Python source code are in ranifall folder. This app need two parameters named location and url (api url where real-time weather info is available). 
The parameters are stored in rainfall/app.config file. </p>

### Run this application on local machine for testing
If we want to run this application on our local machine directly without docker then we need to  
1. Install python3  
2. Install modules listed in requirements.txt. 
  ```pip3 install -r requirements.txt``` 
3. Start application ``` python3 rainfall/flask_app.py ```  
4. App can be access on http://127.0.0.1:5000  once service starts successfully. 


### Run this app as a docker container 
<p>This application can be deployed as a docker container. Clone this repo and create a docker image.

*We can build the image from the following command.*
```
docker build -t <docker-image-name>:<version> .
```
*We need to push docker image to docker registry if we want to deploy in kubernetes.*

```
docker tag <docker-image-name>:<version> <docker-registry>/<docker-image-name>:<version>
docker push <docker-registry>/<docker-image-name>:<version>
```

In this docker based app, Ngnix is acting as a front end reverse proxy and listening on port 8080.
</p>

### Kubernetes yaml file
<p> kubernetes yaml files are located in k8s folder. 
1. update the docker image information in pod.yaml file.
2. update location in configMap.yaml *available location can be found at https://api.data.gov.sg/v1/environment/rainfall* </p>

### Deploy docker image on kubernetes

*Run below command from repo root dir to deploy config map.*
```
kubectl apply -f k8s/configMaps.yaml 
```
*Run below command from repo root dir to deploy pod named rainfall.*
```
kubectl apply -f k8s/pod.yaml
```

**Verification**
1. exec into pods ```kubectl exec -it rainfall -- bash```
2. run curl to check webpage ```curl -v http://localhost:8080```

*Further we can create a k8s service to access webpage from outside pod.*
