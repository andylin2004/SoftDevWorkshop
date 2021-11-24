from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
import urllib.request
import json

app = Flask(__name__)    #create Flask object


@app.route("/")
def disp_loginpage():
    apiKey = open('key_nasa.txt', 'r').readline()
    url = "https://api.nasa.gov/planetary/apod?api_key="+apiKey
    siteData = urllib.request.urlopen(url)
    data = json.load(siteData)
    return render_template( 'main.html' ) # Render the login template


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()