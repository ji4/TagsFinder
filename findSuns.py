# !/usr/bin/python
# coding:utf-8
import os
from os import listdir
from os.path import isfile, join
from bs4 import BeautifulSoup
import re

#filePath = '/Users/money/Documents/GitHub/cdcMain/pages/13_1_new_cluster_report.html'
dirPath = '/Users/money/Documents/GitHub/cdcMain/pages/'
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
	
def findPreviousSibling(tag):
	print 'codingMemo: '
	print tag.codingMemo
	print '\n'
	
	if tag.find_previous_sibling() is None: #previous tag's suffix is text
		print 'A previous tag with "text" suffix found: '
		print tag.previousSibling
		print '\n'
		return tag.previousSibling
	print 'A previous tag with "tag" suffix found: '
	print tag.find_previous_sibling()
	return tag.find_previous_sibling() #previous tag's suffix is a closed tag

def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def extractTags(sun_tags):
	aryTags = []
	for sun_tag in sun_tags:
		#extract codingMemo
		attrValue = sun_tag.attrs[tagAttr]
		
		if completeLinkPattern in attrValue:#https://ca.....
			if strAttrSplitValue in attrValue:#....strMemo=....https://ca.....
				codingMemo = attrValue.split('codingMemo.html?strMemo=', sliceNum)[index]
			else:
				codingMemo = attrValue
		elif strAttrSplitValue in attrValue:#....strMemo=....
			codingMemo = attrValue.split(strAttrSplitValue, sliceNum)[index]
		else:
			codingMemo = attrValue
		codingMemo = codingMemo.replace('\n', ' ').replace('\r', '')
		sun_tag.codingMemo = codingMemo

		#create a new object
		objTag = ObjTag()
		
		#store value into object
		objTag.codingMemo = codingMemo
		
		previous_tag = findPreviousSibling(sun_tag)
		if isinstance(previous_tag, basestring): # is string
			objTag.previousSibling = previous_tag.strip()
		elif previous_tag is not None: #is a tag
			if remove_html_tags(previous_tag.text).strip() == '*':#find previous tag if it is *
				previous_tag = previous_tag.previousSibling
				objTag.previousSibling = previous_tag.strip()
			else:
				objTag.previousSibling = remove_html_tags(previous_tag.text)
			
		
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