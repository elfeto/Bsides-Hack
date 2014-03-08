#####################
#				    #
# Put all functions #
#				   	#
#####################


import re
import os.path
import string
import hashlib

def buildHash(array):
	md5 = hashlib.md5()
	md5.update(array)
	csig = md5.hexdigest()
	return csig
	

def fileParser(path, signatures, keywords):
	import hashlib
	logfile = open(path, 'r')
	ipC = {}
	for lines in logfile:
		split_line = splitLine(lines)
		keys, sigs, error = parseLine(split_line, signatures,keywords)
	
		# IP counter for ip graph.
		if not ipC.has_key(split_line["ip"]):
			ipC[split_line["ip"]] +=1 
		else:
			ipC[split_line["ip"]] = 1	
				
		#print logger

def splitLine(lines):
	lines = lines.split(' ')

	dic = {}
	dic['ip'] = lines[0]
	date = lines[3]
	dic['date'] = date[1:-1]
	dic['type'] = lines[5]
	dic['string'] = lines[6]
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
	print splitted_url
	for i in range(url_len):
		current_str = string.join(splitted_url[i:], "/")
		c_sig = buildHash(current_str)
		if c_sig in signatures:
			sig_found.append((c_sig, current_str))	
		print current_str, c_sig

	return key_found, sig_found, None
			
	
