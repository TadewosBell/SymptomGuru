import requests
from bs4 import BeautifulSoup

from flask import Flask


def PageScrape():

	page = requests.get("http://www.rightdiagnosis.com/surgery/abdominal-liposuction.htm")

	soup = BeautifulSoup(page.content, 'html.parser')

	procedure = soup.find(id='wd_content')

	title = soup.findAll('h1')

	pElement = {}

	subtitlesW = soup.find_all('h2')
	
	subtitles = []
	
	for i in subtitlesW:
		subtitles.append(i.get_text())

	pElement[title[0].get_text()] = subtitles

       #print (pElement)

	
	Dsc = []
	#for i in subtitles:
		#	Desc.append(soup.find(text = i.get_text()).findNext('p').contents)

	#for x in Desc:
		#print x

	return pElement
