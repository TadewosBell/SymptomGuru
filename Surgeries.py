import requests
from bs4 import BeautifulSoup

page = requests.get("http://www.rightdiagnosis.com/surgery/abdominal-liposuction.htm")

soup = BeautifulSoup(page.content, 'html.parser')

procedure = soup.find(id='wd_content')

title = soup.findAll('h1')

print(title)

subtitles = soup.find_all('h2')

print(subtitles)

Dsc = []
#for i in subtitles:
#	Desc.append(soup.find(text = i.get_text()).findNext('p').contents)

#for x in Desc:
	#print x
