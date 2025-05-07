# Base Images
FROM ubuntu:latest

# nignx install
RUN apt -y update && apt -y upgrade
RUN apt -y install nginx
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf
RUN chown -R www-data:www-data /var/lib/nginx

VOLUME ["/data", "/etc/nginx-site-enabled", "/var/log/nginx"]

WORKDIR /etc/nginx

# Port
EXPOSE 80
EXPOSE 443

# Server Exection
CMD ["nginx"]
