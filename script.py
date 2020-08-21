import os
import time
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

#download and extract chromedriver executable and provide the location to the same below
# link for chromedriver zip - https://chromedriver.storage.googleapis.com/index.html?path=84.0.4147.30/
chromedriver = "C:/Users/Vivek Vamsi/Desktop/chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
d = webdriver.Chrome(chromedriver,options=chrome_options) 

#just enter relavant username and password. also enter url for folder you wish to download
username = "user"
password = "pass"
url = "https://www.bphc4.ml/0:/Ultimate%20Server/TV%20Shows/TV%20Shows%20English/S/Silicon%20Valley%20(2014)/S06/Silicon.Valley.S06E07.iNTERNAL.1080p.WEB.H264-AMRAP/"

if(url.startswith("https://www.")):
	urlWithAuth = "https://" + username + ":"+ password+ "@" + url[8:]
else:
	urlWithAuth = "https://www." + username + ":"+ password+ "@" + url
	
d.get(urlWithAuth)

time.sleep(7)
page_html = d.page_source
soup = BeautifulSoup(page_html, 'html.parser')
res = soup.findAll('td',{"class":"td-item"})
content = []
for result in res:
	try:
		content.append(result.attrs['title'])
	except KeyError:
		continue

for item in content:
	linkappended = url + item
	stringcmd = "cmd /c wget --user="+username +" --password=" +password +" "+ linkappended
	os.system(stringcmd)