Remarkable Divers - Andy Lin, Qina Liu, Roshani S
SoftDev
K25 - making Apache2 serve a flask app
2022-01-19
time spent: 5

if wsgi is missing:

sudo apt-install libapache2-mod-wsgi
then sudo a2enmod wsgi, sudo systemctl restart apache2
verify with sudo apache2ctl -t -D DUMP_MODULES

super important: apache2 will only serve up flask apps when the main script file is named __init__.py

mv can be used to rename files as well (just use mv [original name] [new name])
how to make apache2 serve up a flask app

1. enable wgsi via sudo apt-get install libapache2-mod-wsgi-py3 python-dev and sudo a2enmod wsgi
2. set up the filesystem for the flask app:
    cd /var/www
    sudo mkdir FlaskApp (or something else)
    cd FlaskApp
    sudo mkdir FlaskApp
    [during this step, get the contents of project you want to serve up over to the current directory]
    (you may also need to modify app.run to say app.run(host='0.0.0.0'))
3. install flask via sudo apt-get install python3-pip and sudo pip3 install virtualenv
4. create a new virtual environment in the created FlaskApp directory via python3 -m venv [where you want the venv to be and the name at the end] and activate it
5. install flask in the virtual environment and verify to see if it works
6. create virtual host file via sudo nano /etc/apache2/sites-available/[the name you want to call it].conf
    paste this whole thing:
    <VirtualHost *:80>
        ServerName mywebsite.com
        ServerAdmin admin@mywebsite.com
        WSGIScriptAlias / /var/www/FlaskApp/flaskapp.wsgi
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
    (you can also get away with changing mywebsite to the ip address and change the parent flaskapp directory name to something else, but match it to the mkdir name from earlier)
7. enable virtual host by sudo a2ensite [conf name]
8. create wsgi file via cd /var/www/FlaskApp (for last part, or the name you made in mkdir) and sudo nano flaskapp.wsgi
    paste this in:
    #!/usr/bin/python
    import sys
    import logging
    logging.basicConfig(stream=sys.stderr)
    sys.path.insert(0,"/var/www/FlaskApp/")

    from FlaskApp import app as application
    application.secret_key = 'Add your secret key'
9. apt-get time:
    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get install python3-pip
    sudo apt-get install python3-dev
    sudo apt-get install python3-setuptools
    sudo apt-get install python3-venv
    sudo apt-get install build-essential libssl-dev libffi-dev
    sudo apt-get install libapache2-mod-wsgi-py3
10. more packages time:
    pip install wheel 
    pip install flask
    pip install uwsgi
    pip install requests
11. maybe restart via sudo service apache2 restart 
12. if you want to test, do sudo ufw allow 5000 and run the flask app script in the created venv and load up the site via the ip address:5000

source: room 5's instructions and https://github.com/ElizaKnapp/workshop-repo/blob/main/25_flask-apache/README.md (via https://pythonforundergradengineers.com/flask-app-on-digital-ocean.html and https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps)