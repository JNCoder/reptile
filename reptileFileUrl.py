#!/usr/bin/python

from helper import *
from lxml import etree

class reptileFileUrl:
	def __init__(self):
		pass
		
	def getFileUrlByDetailUrl(self, detailUrl):
		detailContent = helper.getHtmlByUrl(detailUrl, proxies=helper.getProxies())
		flashUrl = self.resolveDetailContent(detailContent)
		vid = helper.getParmsFromUrl(flashUrl)['VID']
		swfUrl = 'http://91.9p91.com/getfile_jw.php?VID={0}'.format(vid)
		swfContent = helper.getHtmlByUrl(swfUrl)
		return self.resolveSwfContent(swfContent)
		
	def resolveDetailContent(self, detailConetnt):
		page = etree.HTML(detailConetnt)
		linkParams = page.xpath(u'//*[@id="fm-video_link"]/text()')
		return linkParams[1]
		
	def resolveSwfContent(self, content):
		startIndex = content.index('file=') + 5
		fileUrl = content[startIndex:len(content)]
		fileUrl = fileUrl.replace('.mp4&','.mp4?')
		return fileUrl
		
print(reptileFileUrl().getFileUrlByDetailUrl('http://91p02.space/view_video.php?viewkey=d0f6bdef640691dd0625&page=118&viewtype=basic&category=mf'))