import requests
from bs4 import BeautifulSoup
import re
from lxml import html
from flask import Flask, jsonify
from flask_pymongo import PyMongo
import json

surgeries = {}

def PageScrape(link):

	Baseurl = "http://www.rightdiagnosis.com"
	
	url = Baseurl + link
	page = requests.get(url)

	tree = html.fromstring(page.content)

	diseaseTreated(tree)

def diseaseTreated(tree):
	
	title = tree.xpath('//*[@id="wd_content"]/h1')

	h2 = tree.xpath('//*[@id="wd_content"]/h2')

	conditions = tree.xpath('//*[@id="wd_content"]/ul[1]/li')

	conditionsLink = tree.xpath('//*[@id="wd_content"]/ul[1]/li/a')

	name = title[0].text

	conditionsList = []
	conditionsList.append("Diseases and Conditions")
	for i in conditions:
		if i.text != None:
			conditionsList.append(re.sub('\n','',i.text))
	subtitles = []
	for i in h2:
		if i.text != None:
			subtitles.append(i.text)

	search = ['Diseases And Conditions Treated','Non-Surgical Options','Other Surgical Options','Procedure Complications','Anesthetic Requirements']
	cntr = 0
	matchText = []
	data = []
	for subs in subtitles:
		for j in search:
			result = re.match(j,subs)
			if result != None:
				#print(result.group(0))
				matchText = []
				matchText.append(result.group(0))
				path = '//*[@id="wd_content"]/ul[' + str(cntr) + ']/li'
				match = tree.xpath(path)
				for i in match:
					if i.text != None:
						matchText.append(re.sub('\n','',i.text))
				path2 = '//*[@id="wd_content"]/ul[' + str(cntr) + ']/li/a'
				match2 = tree.xpath(path2)
				for i in match2:
					if i.text != None:
						matchText.append(re.sub('\n','',i.text)) 
				data.append(matchText)
		
		cntr = cntr + 1		
	

	for i in conditionsLink:
		if i != None:
			conditionsList.append(re.sub('\n','',i.text))

	#	print(name,":",subtitles)


	surgeries[name] = data
	
def allLinks():

	page = requests.get("http://www.rightdiagnosis.com/lists/surgery.htm")

	tree = html.fromstring(page.content)

	names = tree.xpath('//*[@id="wd_content"]/ul/li/a')
	
	links = tree.xpath('//*[@id="wd_content"]/ul/li/a/@href')

	for i in links:
		#print(links[i])
		PageScrape(str(i))

	return surgeries


