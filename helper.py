#coding=utf-8

import requests
import os
from urlparse import urlparse
import json

class helper:
	@staticmethod
	def getHtmlByUrl(url, proxies=None):
		headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
					'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
					'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
					'Accept-Encoding': 'utf-8',
					'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
					'Connection': 'keep-alive'}
		response = None
		if proxies == None:
			response = requests.get(url, headers = headers, timeout = 3, cookies = helper.getCookies())
		else:
			response = requests.get(url, headers = headers, timeout = 3, cookies = helper.getCookies(), proxies=proxies)
			
		return response.content.decode('utf-8', 'ignore')
	
	@staticmethod
	def getCookies():
		f = open(os.path.join(os.path.dirname(os.path.abspath('__file__')),'cookies.txt'),'r')
		cookies = {}
		for line in f.read().split(';'):
			name,value=line.strip().split('=',1)
			cookies[name]=value
		return cookies
		
	@staticmethod
	def getParmsFromUrl(url):
		# query = urlparse.urlparse(url).query
		# return dict([(k,v[0]) for k,v in urlparse.parse_qs(query).items()])
		m = {}
		parsed = urlparse(url)
		for key_value in parsed.query.split('&'):
			m[key_value.split('=')[0]] = key_value.split('=')[1]
		return m
		
	@staticmethod
	def getProxies():
		r = requests.get('http://127.0.0.1:8000/?types=0&protocol=0&country=国内&count=1')
		ip_ports = json.loads(r.text)
		ip = ip_ports[0][0]
		port = ip_ports[0][1]
		return {
				'http':'http://%s:%s'%(ip,port)
				}