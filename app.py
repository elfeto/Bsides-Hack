from flask import Flask, request
from tools import *

app = Flask(__name__) #initializing app

##### Landing Page #####
@app.route("/")
def Landing():
    
    return "Landing Page"


##### Upload Log Page #####
@app.route("/uplog")
def UploadLog():

	return "Upload Log Form"

##### Upload Signature Page #####
@app.route("/upsig")
def UploadLog():

	return "Upload Signature Form"

##### Analyze Page #####
@app.route("/analize")
def Analyze():

	return "Analyze Log and Display output"

##### Store Signature Page #####
@app.route("/signature")
def Signature():

	return "Do something with signature"


if __name__ == "__main__":
    
    app.run()