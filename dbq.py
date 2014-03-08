import MySQLdb

class Queries:

	def getKeywords(self, c):
		keys = []
		query = """select Keyword from keyword where 1"""
		try:
			c.execute(query)
			results = c.fetchall()
			for r in results:
				keys.append(r["keyword"])	
			return keys
		except:
			return None

	def getSignatures(self, c):
		sigs = []
		query = """select * from signature where 1""" 
		try:
			c.execute(query)
			results = c.fetchall()
			for r in results:
				sigs.append(r["Signature"])
			return sigs
		except:
			return None
	
	def searchSignature(self, md5):
		query = """select Signature from signature where Signature == %s""" % md5
		try:
			c.execute(query)
			if c.fetchone():
				return True
			return False
		except:
			return None

	def searchKey(self, key):
		try:
			query = """select Keyword from keyword where Keyword == %s""" % key		
			c.execute(query)		
			if c.fetchone():
				return True
			return False
		except:
			return None
	
	def getSignaturesAll(self, c):
		query = """select * from signature where 1"""
		try:
			c.execute(query)
			return c.fetchall()
		except:
			return None

	def getKeywordsAll(self, c):
		query = """select * from keyword where 1"""
		try:
			c.execute(query)
			return c.fetchall()
		except:
			return None
		
	def delSignature(self, c, sid):
		query = """delete from signature where ID = %s""" % sid
		try:
			c.execute(query)
		except:
			pass

	def delKeyword(self, c, kid):
		query = """delete from keyword where ID = %s""" % kid
		try:
			c.execute(query)
		except:
			pass
		
		
		
