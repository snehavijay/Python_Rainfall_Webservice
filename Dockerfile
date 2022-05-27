FROM python:3.6
# Create rainfall directory as working directory
WORKDIR /rainfall
# Copy code from root repo to the working directory
COPY rainfall /rainfall
COPY requirements.txt start.sh uwsgi.ini /rainfall/
#Run python commands to build and serve the application
RUN apt-get update && \
    apt-get install -y python3-dev && \
    apt-get install build-essential -y && \
    pip3 install -r requirements.txt && \
    apt-get install nginx -y
#Copying nginx conf file to nginx configuration path
COPY nginx.conf /etc/nginx
#Giving executable permission
RUN chmod 755 /rainfall/start.sh
RUN chown -R www-data /rainfall  /var/log/nginx /etc/nginx /var/lib/nginx /run/
USER www-data
ENTRYPOINT ["bash", "/rainfall/start.sh"]