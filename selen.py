
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time   
from bs4 import BeautifulSoup
import requests


driver = webdriver.Firefox()
driver.get("https://www.youtube.com/playlist?list=PL1pf33qWCkmibUP3X3Xah-vGZk0MLhu-B")

def url_scrp(ran):
    for i in range(0,ran):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

    sourceCode = driver.page_source
    return sourceCode

def getPlaylistLinks(sourceCode):
    soup = BeautifulSoup(sourceCode, 'html.parser')
    domain = 'https://www.youtube.com'
    linkList = []
    for link in soup.find_all("a", {"dir": "ltr"}):
        href = link.get('href')
        if href.startswith('/watch?'):
            #print(link.string.strip())
            #print(domain + href + '\n')
            linkList.append(domain + href)
    return linkList

sourceCode = url_scrp(5)

print(sourceCode)
list = getPlaylistLinks(sourceCode)

print(len(list))