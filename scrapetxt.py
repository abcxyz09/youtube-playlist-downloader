from bs4 import BeautifulSoup
from pytube import YouTube
import requests


pathToSave = input('Enter Path Where You Want to Save Your Videos: ')

skipVideo = int(input('Enter a Number of Skipped Videos: '))

videoLinkList = []

try:
    with open("doc.txt") as doc:
        sourceCode = doc.read()
        try:
            soup = BeautifulSoup(sourceCode, 'html.parser')
            domain = 'https://www.youtube.com'
            for link in soup.find_all("a",attrs={'class':'ytd-playlist-video-renderer'}):
                href = link.get('href')
                videoLinkList.append(href)
                #print(href)
           
                
        except Exception as e:
            print("Request Error: " + url)
        doc.close()

except Exception as e:
    print('File Opening Error.')

counter = 0

print('Total Video: ' + str(len(videoLinkList)))

for link in videoLinkList:
    counter = counter + 1
    if counter > skipVideo:
        try:
            yt = YouTube(link)
            print('downloading........')
            print(str(counter) + ": " + yt.title)
            yt.streams.filter(progressive=True, file_extension='mp4',res='360p').order_by('resolution').desc().first().download(pathToSave)
            print('download completed.')
        except Exception as e:
            print("Error: " + link)