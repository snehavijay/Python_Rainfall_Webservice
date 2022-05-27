# Webservice to display real-time raining data for a particular location.

### This application using the Python, Flask, uWSGI and Nginx. 

<p>This app will fetch the real-time weather info from https://api.data.gov.sg/v1/environment/rainfall and display the raining data for given location.
This app need two parameters named location and url (api url where real-time weather info is available). 
The parameters are stored in app.config file.
</p>

<p>This is docker based application. Clone this repo and create a docker image. 

*We can build the image from the following command.*
'''
docker build -t <docker-image-name>:<version> .
'''
*We need to push docker image to docker registry if we want to deploy in kubernetes.*
'''
docker tag <docker-image-name>:<version> <docker-registry>/<docker-image-name>:<version>
docker push <docker-registry>/<docker-image-name>:<version>
'''


In this docker based app, Ngnix is acting as a front end reverse proxy and listening on port 8080.
</p>

### Creating Kubernetes yaml file

### Deployment on kubernetes


