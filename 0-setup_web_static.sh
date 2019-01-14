#!/usr/bin/env bash
# sets up servers for deployment of web_static
if ! dpkg -s nginx; then
	sudo apt-get -y update
	if sudo apt-get -y install nginx; then
		cp /etc/nginx/sites-available/default{,.original}
		PLACE=$(grep -m 1 'root' /etc/nginx/sites-available/default | cut -d ' ' -f2 | tr -d ';')
		sudo bash -c 'echo "Holberton School" > "'"$PLACE"'/index.html"'
		new="location ~ '/redirect_me(?=\/|)' {\n\t\treturn 301 https://qz.com/;\n\t}"
		sudo sed -i "/^\tserver_name localhost;$/a \\\n\\t$new" /etc/nginx/sites-available/default
		new="\t\terror_page 404 @my404;"
		sudo sed -i "/^\tlocation \/ {$/a \\$new" /etc/nginx/sites-available/default
		new="location @my404 {\n\t\tdefault_type text/html;\n\t\treturn 404 \"Ceci n'est pas une page\\\n\\\n\";\n\t}"
		sudo sed -i "/^\tserver_name localhost;$/a \\\n\\t$new" /etc/nginx/sites-available/default
	fi
fi
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
sudo bash -c 'echo "DOGGY DOG WORLD" > /data/web_static/releases/test/index.html'
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
cp /etc/nginx/sites-available/default{,.originalver2}
sed -E -i "\|^\tserver_name localhost;$|a\\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default
service nginx restart
