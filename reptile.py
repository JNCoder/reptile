#coding=utf-8

import requests
from lxml import etree
from DBDataAccess import *
from helper import *

class reptile:
	
	repeatCount = 0
	
	def getListHtmlByPageHtml(self, content):
		listHtml = etree.HTML(content.lower()).xpath(u'//*[@class="listchannel"]')
		return listHtml

	def getItemByItemHtml(self, itemHtml):
		imageUrl = itemHtml.xpath(u'./div[1]/a[1]/img[1]/@src')[0]
		url = itemHtml.xpath(u'./a[1]/@href')[0]
		title =  itemHtml.xpath(u'./a[1]/@title')[0]
		time = itemHtml.xpath(u'./span[1]/following-sibling::text()')[0]
		time = time.replace('\n','')
		time = time.strip().encode("utf-8")
		authorUrl = itemHtml.xpath(u'./a[2]/@href')[0]
		authorID = helper.getParmsFromUrl(authorUrl)['uid']
		author = itemHtml.xpath(u'./a[2]/text()')[0]
		uploadTime = itemHtml.xpath(u'./span[2]/following-sibling::text()')[0]
		uploadTime = uploadTime.replace(' ','')
		seeCount = itemHtml.xpath(u'./span[4]/following-sibling::text()')[0]
		seeCount = seeCount.replace('\n','')
		seeCount = seeCount.replace(' ','')
		seeCount = seeCount[0:len(seeCount)-2]
		favoriteCount = itemHtml.xpath(u'./span[5]/following-sibling::text()')[0]
		favoriteCount = favoriteCount.replace(' ','')
		commentCount = itemHtml.xpath(u'./span[5]/following-sibling::text()')[0]
		commentCount = commentCount.replace(' ','')

		return {'imageUrl':imageUrl, 
		    		 'url':url,
					 'title':title, 
					 'authorUrl':authorUrl, 
		'author':author, 
		'time':time, 
		'uploadTime':uploadTime, 
		'seeCount':seeCount, 
		'favoriteCount':favoriteCount, 
		'commentCount':commentCount}
	
	def getContentByUrl(self, url):
		try:
			html = helper.getHtmlByUrl(url)
			listHtml = self.getListHtmlByPageHtml(html)
			for itemHtml in listHtml:
				item = self.getItemByItemHtml(itemHtml)
				if not DBDataAccess.instance().exists(item['title']):
					DBDataAccess.instance().add(item)
			self.repeatCount = 0
		except Exception, e:
			self.repeatCount = self.repeatCount + 1;
			if self.repeatCount < 3:
				print(e.message)
				self.getContentByUrl(url)
			
	def allReptile(self):
		for pageIndex in range(858, 3424):
			self.getContentByUrl('http://91p02.space/v.php?category=mf&viewtype=basic&page={0}'.format(pageIndex))
			print('第{0}页已爬取'.format(pageIndex))
			
	def updateReptile(self):
		for pageIndex in range(1, 4):
			self.getContentByUrl('http://91p02.space/v.php?category=hot&viewtype=basic&page={0}'.format(pageIndex))
			print('【当前最热】第{0}页已爬取更新'.format(pageIndex))
		print('----------------------------')
		for pageIndex in range(1, 92):
			self.getContentByUrl('http://91p02.space/v.php?category=rf&viewtype=basic&page={0}'.format(pageIndex))
			print('【最近加精】第{0}页已爬取更新'.format(pageIndex))
		print('----------------------------')
		for pageIndex in range(1, 31):
			self.getContentByUrl('http://91p02.space/v.php?category=md&viewtype=basic&page={0}'.format(pageIndex))
			print('【本月讨论】第{0}页已爬取更新'.format(pageIndex))
		print('----------------------------')
		for pageIndex in range(1, 61):
			self.getContentByUrl('http://91p02.space/v.php?category=rp&viewtype=basic&page={0}'.format(pageIndex))
			print('【最近得分】第{0}页已爬取更新'.format(pageIndex))
		
		

reptile().updateReptile()
