#####################
#				    #
# Put all functions #
#				   	#
#####################

def logliner():
	logger = []
	import hashlib
	logfile = open('access_log', 'r')
	for lines in logfile:
		hashing(lines, logger)

def hashing(lines, logger):
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

logliner()