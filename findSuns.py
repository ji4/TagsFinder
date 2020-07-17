# !/usr/bin/python
# coding:utf-8
import os
from os import listdir
from os.path import isfile, join
from bs4 import BeautifulSoup
import re

#filePath = '/Users/money/Documents/GitHub/cdcMain/pages/13_1_new_cluster_report.html'
dirPath = '/Users/money/Documents/GitHub/cdcMain/pages2/'
outputDirPath = '/Users/money/Documents/GitHub/TagsFinder/'
tagAttr = 'href'
tagValue = u'🔆'
completeLinkPattern = '//'
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
	
def findTagsByTagValue(soup, tagValue):
	sun_tags = soup.findAll('a', text = tagValue)
	arySunTags = extractTags(sun_tags)
	return arySunTags
	

	
def extractTags(sun_tags):
	aryTags = []
	for sun_tag in sun_tags:
		#extract codingMemo
		attrValue = sun_tag.attrs[tagAttr]

		if completeLinkPattern in attrValue:
			codingMemo = attrValue
		elif strAttrSplitValue in attrValue:
			codingMemo = attrValue.split(strAttrSplitValue, sliceNum)[index]
		else:
			codingMemo = attrValue
		codingMemo = codingMemo.replace('\n', ' ').replace('\r', '')

		print 'sun_tag.find_previous_sibling(): '
		print sun_tag.find_previous_sibling()
		print '\n'
		
		if sun_tag.find_previous_sibling() is None:
			print 'None previous tag found. Searching previous tag again.'
			print 'A newly found tag: '
			print sun_tag.previousSibling
			print '\n'
			
		print 'codingMemo: '
		print codingMemo
		print '\n'

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
def findSunsInFiles(files):
	for file in files:
		soup = BeautifulSoup(open(dirPath + '/' + file), 'html.parser')
		arySunTags = findTagsByTagValue(soup, tagValue)
		saveToFile(file, arySunTags)

def saveToFile(file, arySunTags):
    with open(outputDirPath + '/output', 'a+') as fLog:
		for sun in arySunTags:

			fLog.write(file + '\t')
			if sun.previousSibling is not None:
				fLog.write(sun.previousSibling.encode('utf-8').strip())
			fLog.write('\t')
			if sun.codingMemo is not None:
				fLog.write(sun.codingMemo.encode('utf-8').strip())
			fLog.write('\n')
			

if __name__ == "__main__":
	htmlFiles = findFiles(dirPath)
	findSunsInFiles(htmlFiles)