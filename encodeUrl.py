#from urllib.parse import unquote
#
#url = 'example.com?title=%D0%BF%D1%80%D0%B0%D0%B2%D0%BE%D0%B2%D0%B0%D1%8F+%D0%B7%D0%B0%D1%89%D0%B8%D1%82%D0%B0'
#print unquote(url)

from urllib import unquote
url = 'example.com?title=%D0%BF%D1%80%D0%B0%D0%B2%D0%BE%D0%B2%D0%B0%D1%8F+%D0%B7%D0%B0%D1%89%D0%B8%D1%82%D0%B0'

url = unquote(url).decode('utf8')
print url


with open('urls.txt','r')as linkFile:
	urls = linkFile.readlines()
	for url in urls:
		url = unquote(url).decode('utf8')
		print url
