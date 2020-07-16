# !/usr/bin/python
# coding:utf-8

from bs4 import BeautifulSoup
import re

filePath = '/Users/money/Documents/GitHub/cdcMain/pages/13_1_new_cluster_report.html'
tagAttr = 'href'
tagValue = u'🔆'
strAttrSplitValue = 'strMemo='


soup = BeautifulSoup(open(filePath), 'html.parser')

def findTagsByTagValue(tagValue):
	sun_tags = soup.findAll('a', text = tagValue)
	getSunHrefValueByTags(sun_tags)
	
def getSunHrefValueByTags(sun_tags):
	for sun_tag in sun_tags:
		attrValue = sun_tag.attrs[tagAttr]
		codingMemo = attrValue.split(strAttrSplitValue,1)[1]
		print codingMemo

if __name__ == "__main__":
	findTagsByTagValue(tagValue)