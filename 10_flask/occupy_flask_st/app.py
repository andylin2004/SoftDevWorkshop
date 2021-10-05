#Team Name: Hi-C; Yaying Liang Li, Andy Lin, Josephine Lee
#SoftDev
#K10 -- first flask website serving up the outputs of K06's job picker
#2021-10-05

from flask import Flask
from K06 import jobDecider

app = Flask(__name__)

@app.route("/")
def job_decider_web():
    return jobDecider()

app.run()