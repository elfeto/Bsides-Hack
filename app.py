from flask import Flask, request, render_template
from tools import *
from dbq import *

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

	return render_template("uploadsig.html")

##### Analyze Page #####
@app.route("/analyze")
def Analyze():

	chart = GraphTime([('192.168.1.1', 23), ('192.168.2.1', 645)])

	#return chart

	return render_template("analyze.html", chart = str(chart))

##### Store Signature Page #####
@app.route("/signature", methods=['POST'])
def Signature():

	signature = request.form['signature']

	status = None

	try:

		db= MySQLdb.connect(host="localhost",user="bsides", passwd="lamadredelquemerompaestepassword",db="Bsides")
	
		c = db.cursor(MySQLdb.cursors.DictCursor)

		status = insertSignature(c, signature);

		c.close()

	except:

		pass

	return render_template("signature.html", status = status)


if __name__ == "__main__":
    
    app.run()