#!/usr/bin/env bash
# Sets up a web server for deployment of web_static.

apt-get update
apt-get install -y nginx

# Create directories for web_static releases and shared files
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create a simple index.html file in the test directory
echo "Holberton School" > /data/web_static/releases/test/index.html

# Create a symbolic link from current to the test directory
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change ownership and group of the directories to user "ubuntu"
chown -R ubuntu /data/
chgrp -R ubuntu /data/

# Configure Nginx server block for web_static
printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

# Restart Nginx service to apply the configuration changes
service nginx restart
