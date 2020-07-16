# !/usr/bin/python
# coding:utf-8
import os
from os import listdir
from os.path import isfile, join
from bs4 import BeautifulSoup
import re

#filePath = '/Users/money/Documents/GitHub/cdcMain/pages/13_1_new_cluster_report.html'
dirPath = '/Users/money/Documents/GitHub/cdcMain/pages/'
tagAttr = 'href'
tagValue = u'🔆'
strAttrSplitValue = 'strMemo='
sliceNum = 1
index = 1



class ObjTag:
	def __init__(self):
		self._codingMemo = None
		self._previousSibling = None
	@property
	def codingMemo(self):
		return self._codingMemo
	
	@property
	def previousSibling(self):
		return self._previousSibling
	
	@codingMemo.setter
	def codingMemo(self, codingMemo):
		self._codingMemo = codingMemo
		
	@previousSibling.setter
	def previousSibling(self, previousSibling):
		self._previousSibling = previousSibling
	
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
		print 'attrValue: '
		print attrValue
		print '\n'
		if strAttrSplitValue in attrValue:
			codingMemo = attrValue.split(strAttrSplitValue, sliceNum)[index]
		else:
			codingMemo = attrValue
			

		#create a new object
		objTag = ObjTag()
		
		#store value into object
		objTag.codingMemo = codingMemo
		
		if isinstance(sun_tag.previousSibling, basestring):
			objTag.previousSibling = sun_tag.previousSibling.strip()
		else:
			objTag.previousSibling = sun_tag.previousSibling
		aryTags.append(objTag)
		
	return aryTags

def findFiles(path):
	return [f for f in listdir(path) if isfile(join(path, f))]

if __name__ == "__main__":
	htmlFiles = findFiles(dirPath)
	print htmlFiles
	for file in htmlFiles:
		print 'current file: '
		print file
		soup = BeautifulSoup(open(dirPath + '/' + file), 'html.parser')
		findTagsByTagValue(tagValue)