#! /usr/bin/env python
#coding=utf-8

from pymongo import MongoClient

class DBDataAccess(object):
	def __init__(self):
		self.connect()
	
	@staticmethod 
	def instance():
  		if not hasattr(DBDataAccess, "_instance"):
			# with DBDataAccess._instance_lock:
			if not hasattr(DBDataAccess, "_instance"):
				# New instance after double check
				DBDataAccess._instance = DBDataAccess()
		return DBDataAccess._instance
	db = None
	@classmethod
	def connect(self):
		try:
			conn = MongoClient('localhost', 27017)
			self.db = conn['91']
			self.db.authenticate('jncoder','nwyfss')
			print('connect db successed!')
		except Exception, e:
			print('connect error:{0}'.format(e.message))
	def add(self, item):
		try:
			self.db['movies'].insert(item)
		except Exception, e:
			raise e
	def exists(self, title):
		u2 = self.db['movies'].find_one({"title":title})
#		print(title)
#		if title == u'C仔-超高级的爆乳(经典作品)':
#			if u2 == None:
#				print('未找到')
#			else:
#				print('找到')
		return u2 != None
#	def query(self, sql):
#		try:
#			return self.get_cursor().execute(sql).fetchall()
#		except Exception, e:
#			raise e
#	def commit(self):
#		try:
#			self.conn.commit()
#		except Exception, e:
#			raise e
