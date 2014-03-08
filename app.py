from flask import Flask, request, render_template
from tools import *
#from dbq import *
import time
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'uploads'
app = Flask(__name__) #initializing app
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.debug = True

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

	return render_template("uploadsig.html")


##### Upload Signature Page #####
@app.route("/upkey")
def UploadKey():

	return render_template("uploadkey.html")

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

		#Connect to mysql db
		db= MySQLdb.connect(host="localhost",user="bsides", passwd="lamadredelquemerompaestepassword",db="Bsides")
		#Returns results in dictionary form
		c = db.cursor(MySQLdb.cursors.DictCursor)
		#Constructor Queries()
		quer = Queries()
		#Parse Log file uploaded
		var1, var2, var3 = fileParser(os.path.join(app.config['UPLOAD_FOLDER'], filename), quer.getSignatures(c), quer.getKeywords(c))

		#Create ip time acess chart
		ipChart = GraphIp(var2)
		#Create time acess chart
		timeChart = GraphTime(var1)

	except:

		pass

	return render_template("analyze.html", ip = ipChart, time = timeChart, reports =reports)
	

##### Store Signature Page #####
@app.route("/signature", methods=['POST'])
def Signature():

	signature = request.form['signature']

	status = None

	try:

		db= MySQLdb.connect(host="localhost",user="bsides", passwd="lamadredelquemerompaestepassword",db="Bsides")
	
		c = db.cursor(MySQLdb.cursors.DictCursor)

		quer = Queries()

		status = quer.insertSignature(c, signature);

		db.commit()

		c.close()

	except:

		pass

	return render_template("signature.html", status = status)


##### Store Key Page #####
@app.route("/key", methods=['POST'])
def Key():

	key = request.form['key']

	status = None

	try:

		db= MySQLdb.connect(host="localhost",user="bsides", passwd="lamadredelquemerompaestepassword",db="Bsides")
	
		c = db.cursor(MySQLdb.cursors.DictCursor)

		quer = Queries()

		status = quer.insertKey(c, key);

		db.commit()

		c.close()

	except:

		pass

	return render_template("key.html", status = status)

if __name__ == "__main__":
    
	#app.run()

    app.run(host='136.145.181.51', port=80)
