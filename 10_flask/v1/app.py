#Team Name: Hi-C; Yaying Liang Li, Andy Lin, Josephine Lee
#SoftDev
#K10 -- analyzing the different versions of flask sample code
#2021-10-05

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()

# The changes made here were that the terminal didn't print any statements, as no print statements were called. The "no hablo queso" did show up on the web page, though.
# A warning is thrown on the fact that it is a development server and not push it to production though.
