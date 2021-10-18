# Team Name: Sleepy Programmers: Andy Lin, Shadman Rakib, Raymond Yeung
# SoftDev
# K14 -- Forms using Flask
# 2021-10-14

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

app = Flask(__name__)    #create Flask object


@app.route("/")
def disp_loginpage():
    return render_template( 'login.html' ) # Render the login template


@app.route("/auth", methods=['GET', 'POST']) # , methods=['GET', 'POST'])
def authenticate():
    # The requests property contains the values property. The value property contains
    # data from both requests.args and requests.form. 
    
    username = request.values['username'] 
    password = request.values['password']

    if username == "dn":
        if password == "1738":
            #response to a person who has the right credentials and logs in
            return render_template('response.html', username=username)
        else:
            return render_template('login.html', error='password')
    else:
        return render_template('login.html', error='username')

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()