from bs4 import BeautifulSoup
import requests

wiki = 'https://en.wikipedia.org/wiki/'

title = input('Enter Wiki Article Title:').strip()

try:
	sourceCode = requests.get(wiki + title).text
	soup = BeautifulSoup(sourceCode,'html.parser')
	for link in soup.find_all('a'):
		href = link.get('href')
		try:
			if href.startswith('/wiki'):
			    articleTitle = link.get('title')
			    print(articleTitle)
		except Exception as e:
			pass
		
		
		

except Exception as e:
	raise e