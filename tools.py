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

def buildHash(array):
	md5 = hashlib.md5()
	md5.update(array)
	csig = md5.hexdigest()
	return csig
	

def fileParser(path, signatures, keywords):
	DateC = {}
	logfile = open(path, 'r')
	for lines in logfile:
		split_line = splitLine(lines)
		keys, sigs, error = parseLine(split_line, signatures,keywords)

		date1 = split_line['date']
		if DateC.has_key(date1[0:6]):
			DateC[date1[0:6]] += 1
		else:
			DateC[date1[0:6]] = 1

	datelist = []
	for key in DateC.keys():
		datelist.append((change(key[3:6])+"/"+key[0:2], DateC[key]))
	datelist.sort()
	print datelist

def change(date):
	if(date == "Jan"):
		return '01'
	if(date == "Feb"):
		return '02'
	if(date == "Mar"):
		return '03'
	if(date == "Apr"):
		return '04'
	if(date == "May"):
		return '05'
	if(date == "Jun"):
		return '06'
	if(date == "Jul"):
		return '07'
	if(date == "Aug"):
		return '08'
	if(date == "Sep"):
		return '09'
	if(date == "Oct"):
		return '10'
	if(date == "Nov"):
		return '11'
	if(date == "Dec"):
		return '12'


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
	if len(line["url"]) > 256:
		return None, None, "URL too long, possible attack"

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

fileParser("access_log","nose","tampoco")

