from flask import Flask, request, render_template
from tools import *

app = Flask(__name__) #initializing app

##### Landing Page #####
@app.route("/")
def Landing():
    
    return render_template('landing.html', name="")

##### Upload Log Page #####
@app.route("/uplog")
def UploadLog():

	return "Upload Log Form"

##### Upload Signature Page #####
@app.route("/upsig")
def UploadSig():

	return "Upload Signature Form"

##### Analyze Page #####
@app.route("/analyze")
def Analyze():

	chart = GraphTime([('192.168.1.1', 23), ('192.168.2.1', 645)])

	#return chart

	return render_template("analyze.html", chart = str(chart))

##### Store Signature Page #####
@app.route("/signature")
def Signature():

	return "Do something with signature"


if __name__ == "__main__":
    
    app.run()