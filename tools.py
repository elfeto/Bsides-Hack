#####################
#				    #
# Put all functions #
#				   	#
#####################

import re
import os.path
import string
import hashlib
import operator

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
	        var chart = new google.visualization.BarChart(document.getElementById('ipchart_div'));
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
	        var chart = new google.visualization.LineChart(document.getElementById('datechart_div'));
	        chart.draw(data, options);
	      }"""

	return chart


keywords = ["sex", "xxx", "porn", "anal"]

def buildHash(array):
	md5 = hashlib.md5()
	md5.update(array)
	csig = md5.hexdigest()
	return csig
	

def fileParser(path, signatures, keywords):
	logfile = open(path, 'r')
	ipC = {}
	DateC = {}
	reports = []
	for lines in logfile:
		split_line = splitLine(lines)
		keys, sigs, error = parseLine(split_line, signatures,keywords)
		if keys or sigs:
			reports.append([split_line["ip"], split_line["date"], split_line["url"], split_line["type"], split_line["id"], keys[:],sigs[:] ])			
				
	
		# IP counter for ip graph.
		if ipC.has_key(split_line["ip"]):
			ipC[split_line["ip"]] +=1 
		else:
			ipC[split_line["ip"]] = 1

		date1 = split_line['date']
		if DateC.has_key(date1[0:6]):
			DateC[date1[0:6]] += 1
		else:
			DateC[date1[0:6]] = 1
				
	ipC = sorted(ipC.iteritems(), key=operator.itemgetter(1))
	DateC = sorted(DateC.iteritems(), key=operator.itemgetter(1))
	ipC = ipC[-30:]

	return DateC, ipC, reports
		

def splitLine(lines):
	lines = lines.split(' ')

	dic = {}
	dic['ip'] = lines[0]
	date = lines[3]
	dic['date'] = date[1:-1]
	dic['type'] = lines[5]
	dic['url'] = lines[6]
	dic['proto'] = lines[7]
	dic['id'] = lines[8]
	
	return dic

def parseLine(line, signatures, keywords):
	
	key_found = []	
	sig_found = []

	# Check length of string (avoid exhaustive attack)
	#if len(line["url"]) > 256:
	#	return None, None, "URL too long, possible attack"

	for key in keywords:
		if re.search(key, line["url"]):
			key_found.append(key)

		
	splitted_url = line["url"].split("/")
	url_len = len(splitted_url)
	for i in range(url_len):
		current_str = string.join(splitted_url[i:], "/")
		c_sig = buildHash(current_str)
		if c_sig in signatures:
			sig_found.append((c_sig, current_str))	

	return key_found, sig_found, None
			
