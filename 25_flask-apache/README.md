# how-to :: Deploy Flask Application on an Ubuntu VPS
---
## Overview
- deploy flask app on our DO servers

### Estimated Time Cost: _

### Prerequisites:
- have a Digital Ocean Droplet with Apache2 

1. Install mod_wsgi (python3 version)
```
$ sudo apt-get install libapache2-mod-wsgi-py3 python-dev
```
2. Enable mod_wsgi
```
$ sudo a2enmod wsgi
```
3. Creating Flask App
```
$ cd /var/www
$ sudo mkdir FlaskApp
$ cd FlaskApp
$ sudo mkdir FlaskApp
$ cd FlaskApp
```
4. Get Your Python Code
- either create __init__.py, git clone a repo, or scp a __init__.py file 
5. Install Flask
```
$ sudo apt-get install python3-pip
$ sudo apt-get install python3-venv
$ python3 -m venv ~/venv
$ source venv/bin/activate
$ sudo pip3 install Flask
```
- test if installation is successful: `$ sudo python3 __init__.py`
- should display "Running on http://127.0.0.1:5000/"; if so success!
```
$ deactivate
```
6. Configure and Enable a New Virtual Host
```
$ sudo nano /etc/apache2/sites-available/FlaskApp.conf 
```
- write this in the file: 
```
<VirtualHost *:80>
		ServerName [DO IP address]
		ServerAdmin user@[DO IP address]
        WSGIScriptAlias / /var/www/FlaskApp/FlaskApp.wsgi
		<Directory /var/www/FlaskApp/FlaskApp/>
			Order allow,deny
			Allow from all
		</Directory>
		Alias /static /var/www/FlaskApp/FlaskApp/static
		<Directory /var/www/FlaskApp/FlaskApp/static/>
			Order allow,deny
			Allow from all
		</Directory>
		ErrorLog ${APACHE_LOG_DIR}/error.log
		LogLevel warn
		CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```
- enable virtual host:
```
$ sudo a2ensite FlaskApp
$ systemctl reload apache2

(to be save)
$ sudo a2ensite FlaskApp
```
7. Create .wsgi File
```
$ cd /var/www/FlaskApp/
$ sudo nano FlaskApp.wsgi
```
- write this in the file:
```
#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/FlaskApp/")

from FlaskApp import app as application
application.secret_key = 'Add your secret key'
```
- restart apache: `$ sudo service apache2 restart`
8. Change directory owner and group
`$ sudo chown -R www-data:www-data/var/www/FlaskApp/FlaskApp`
- Allow the group to write to directory with appropriate permissions
`$ sudo chmod -R 775 /var/www/FlaskApp/FlaskApp`
- Add user to the www-data group
`$ sudo usermod -a -G www-data user`
- logout (exit) and login again
- Check by running `$ ls -al blog within /var/www/FlaskApp/FlaskApp`
    - got `-rwxrwxr-x 1 www-data www-data  136 Jan 20 01:56 __init__.py`
- restart apache: `$ sudo service apache2 restart`

Server Error log can be found at `/var/log/apache2` in the error.log file 
- root access is needed to cd into the apache2 folder and to access its files


1. Step, with [hyperlink](https://xkcd.com)s...


### Resources
* [Digital Ocean Guide](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps)
* Room 5:

---

Accurate as of (last update): 2021-01-19

#### Contributors:  
Andy Lin, pd2  
Roshani Shrestha, pd2  
Qina Liu, pd2  