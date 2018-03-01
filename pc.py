from bs4 import BeautifulSoup
import requests
from pytube import YouTube
import os

def getPlaylistLinks(url):
    sourceCode = requests.get(url).text
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
 
#playlistLink = input('Enter Playlist Link >>>')

#list = getPlaylistLinks(playlistLink)


def readLine():
    filepath = 'link.txt' 
    lin = [] 
    with open(filepath) as fp:  
        line = fp.readline()
        #print(line)
        cnt = 1
        while line:
            l = line.strip()
            if(len(l)>0):
                lin.append(l)
                #print(line.strip())
            #print("Line {}: {}".format(cnt, line.strip()))
            line = fp.readline()
            cnt += 1
    return lin

allPlayLists = readLine()
print(len(allPlayLists))

c = 0

for palyList in allPlayLists:
    playListLinks = getPlaylistLinks(palyList)
    numOfVideo = len(playListLinks)
    path_to_save = '/home/jonyroy/ytd/'+ str(c)+'-'+str(numOfVideo)
    os.makedirs(path_to_save,exist_ok=True)
    #print(len(r))
    c = c + 1


#print(len(list))

#for li in list:
#   print(li)
