from flask import Flask
import sys
sys.path.append('../06_py-csv')
from K06 import jobDecider

app = Flask(__name__)

@app.route("/")
def job_decider_web():
    return jobDecider()

app.run()