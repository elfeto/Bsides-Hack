#####################
#				    #
# Put all functions #
#				   	#
#####################


import re
import os.path
import string
import hashlib

keywords = ["sex", "xxx", "porn", "anal"]

def buildHash(array):
	md5 = hashlib.md5()
	md5.update(array)
	csig = md5.hexdigest()
	return csig
	

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
			
	
