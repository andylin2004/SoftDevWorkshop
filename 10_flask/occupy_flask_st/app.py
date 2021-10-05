from flask import Flask
from K06 import jobDecider

app = Flask(__name__)

@app.route("/")
def job_decider_web():
    return jobDecider()

app.run()