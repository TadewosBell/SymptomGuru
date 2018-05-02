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
	
	procedure = tree.xpath('//*[@id="wd_content"]/ul[1]/li')

	proceduresLink = tree.xpath('//*[@id="wd_content"]/ul[1]/li/a')

	name = title[0].text

	text = []
	for i in procedure:
		if i.text != None:
			text.append(re.sub('\n','',i.text))

	for i in proceduresLink:
		if i !=None:
			text.append(re.sub('\n','',i.text))

	for i in text:
		print(i)
	
	surgeries[name] = text

def allLinks():

	page = requests.get("http://www.rightdiagnosis.com/lists/surgery.htm")

	tree = html.fromstring(page.content)

	names = tree.xpath('//*[@id="wd_content"]/ul/li/a')
	
	links = tree.xpath('//*[@id="wd_content"]/ul/li/a/@href')

	for i in links:
		#print(links[i])
		PageScrape(str(i))

	return surgeries

