#####################
#				    #
# Put all functions #
#				   	#
#####################

import re
import os.path
import string
import hashlib

def GraphIp(tupleList):
	
	chart =""" 
	      google.load('visualization', '1.0', {'packages':['corechart']});
	      google.setOnLoadCallback(drawChart);
	      function drawChart() {
	        var data = new google.visualization.DataTable();
	        data.addColumn('string', 'ipaddress');
	        data.addColumn('number', 'access');
		        data.addRows([ """

	if len(tupleList) != 0: 
		for ip,access in tupleList:
			chart += "['%s', %s]," % (ip,access)
	        chart += "]);"

	chart +="""var options = {'title':'IP address | access',
	                       'width':400,
	                       'height':300};
	        var chart = new google.visualization.BarChart(document.getElementById('chart_div'));
	        chart.draw(data, options);
	      }"""

	return chart

def GraphTime(tupleList):
	
	chart = """ 

	      // Load the Visualization API and the piechart package.
	      google.load('visualization', '1.0', {'packages':['corechart']});

	      // Set a callback to run when the Google Visualization API is loaded.
	      google.setOnLoadCallback(drawChart);

	      // Callback that creates and populates a data table,
	      // instantiates the pie chart, passes in the data and
	      // draws it.
	      function drawChart() {

	        // Create the data table.
	        var data = new google.visualization.DataTable();
	        data.addColumn('string', 'time');
	        data.addColumn('number', 'access');
		        data.addRows([ """

	if len(tupleList) != 0: 
		for time,access in tupleList:
			chart += "['%s', %s]," % (time,access)
	        chart += "]);"

	chart += """

	        // Set chart options
	        var options = {'title':'Time | access',
	                       'width':400,
	                       'height':300};

	        // Instantiate and draw our chart, passing in some options.
	        var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
	        chart.draw(data, options);
	      }"""

	return chart


keywords = ["sex", "xxx", "porn", "anal"]

def buildHash(array):
	md5 = hashlib.md5()
	md5.update(array)
	csig = md5.hexdigest()
	return csig
	

def fileParser(path):
	import hashlib
	logfile = open(path, 'r')
	for lines in logfile:
		logger = []
		splitLine(lines, logger)
		#print logger

def splitLine(lines, logger):
	lines = lines.split(' ')

	dic = {}
	dic['ip'] = lines[0]
	logger.append(dic['ip']) #ip
	date = lines[3]
	dic['date'] = date[1:-1]
	logger.append(dic['date']) #fecha
	dic['type'] = lines[5]
	logger.append(dic['type']) #type
	dic['string'] = lines[6]
	logger.append(dic['string']) #string
	dic['proto'] = lines[7]
	logger.append(dic['proto']) #protocolo
	dic['id'] = lines[8]
	logger.append(dic['id']) #access-id

def parseLine(line, signatures, keywords):
	
	key_found = []	
	sig_found = []

	# Check length of string (avoid exhaustive attack)
	if len(line["url"]) > 256:
		return None, None, "URL too long, possible attack"

	for key in keywords:
		if re.search(key, line["url"]):
			key_found.append(key)

		
	splitted_url = line["url"].split("/")
	url_len = len(splitted_url)
	print splitted_url
	for i in range(url_len):
		current_str = string.join(splitted_url[i:], "/")
		c_sig = buildHash(current_str)
		if c_sig in signatures:
			sig_found.append((c_sig, current_str))	
		print current_str, c_sig

	return key_found, sig_found
			
