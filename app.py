from flask import Flask, request, render_template
from tools import *
import time
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'uploads'
app = Flask(__name__) #initializing app
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

##### Landing Page #####
@app.route("/")
def Landing():
    
    return render_template('landing.html', name="")

##### Upload Log Page #####
@app.route("/uplog")
def UploadLog():

	return render_template('uploadlog.html')

##### Upload Signature Page #####
@app.route("/upsig")
def UploadSig():

	return "Upload Signature Form"

##### Analyze Page #####
@app.route("/analyze", methods=['POST'])
def Analyze():
	#Get form file
	file = request.files['log-file']
	#Create secure filename
	filename = "log-" + str(time.time())
	#Save the file
	file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

	try:

		db= MySQLdb.connect(host="localhost",user="bsides", passwd="lamadredelquemerompaestepassword",db="Bsides")

		c = db.cursor(MySQLdb.cursors.DictCursor)

		quer = Queries()

		var = fileParser(os.path.join(app.config['UPLOAD_FOLDER'], filename), quer.getSignatures(c), quer.getKeywords(c))

		chart = GraphTime(var)

	except:

		pass

	return render_template("analyze.html", chart = chart)
	

##### Store Signature Page #####
@app.route("/signature")
def Signature():

	return "Do something with signature"


if __name__ == "__main__":
    
    app.run()