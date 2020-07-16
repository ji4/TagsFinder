# !/usr/bin/python
# coding:utf-8

from bs4 import BeautifulSoup
import re

filePath = '/Users/money/Documents/GitHub/cdcMain/pages/13_1_new_cluster_report.html'
tagAttr = 'href'
tagValue = u'🔆'
strAttrSplitValue = 'strMemo='


soup = BeautifulSoup(open(filePath), 'html.parser')

class ObjTag():
	def __init__(self):
		self.codingMemo = ''
#		self.previousSibling = 
	def addCodingMemo(self, codingMemo):
		self.codingMemo = codingMemo
	def addPreviousSibling(self, previousSibling):
		self.previousSibling = previousSibling
	
def findTagsByTagValue(tagValue):
	sun_tags = soup.findAll('a', text = tagValue)
	arySunTags = extractTags(sun_tags)
	for s in arySunTags:
		print '\ns.codingMEmo: ' + s.codingMemo
		print 'previous sibling: ' 
		print s.previousSibling

	
def extractTags(sun_tags):
	aryTags = []
	for sun_tag in sun_tags:
		#extract codingMemo
		attrValue = sun_tag.attrs[tagAttr]
		codingMemo = attrValue.split(strAttrSplitValue,1)[1]

		#create a new object
		objTag = ObjTag()
		
		#store value into object
		objTag.codingMemo = codingMemo
		
		if isinstance(sun_tag.previousSibling, basestring):
			objTag.addPreviousSibling(sun_tag.previousSibling.strip())
		else:
			objTag.addPreviousSibling(sun_tag.previousSibling)
		aryTags.append(objTag)
		
	return aryTags
		

if __name__ == "__main__":
	findTagsByTagValue(tagValue)