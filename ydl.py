from bs4 import BeautifulSoup
import requests
from pytube import YouTube
import os

def getPlaylistLinks(url):
    linkList = []
    try:
        sourceCode = requests.get(url).text
        soup = BeautifulSoup(sourceCode, 'html.parser')
        domain = 'https://www.youtube.com'
        for link in soup.find_all("a", {"dir": "ltr"}):
            href = link.get('href')
            if href.startswith('/watch?'):
            #print(link.string.strip())
            #print(domain + href + '\n')
                linkList.append(domain + href)
        return linkList
    except Exception as e:
        print("Request Error: " + url)
        return linkList
    

def show_progress(stream, chunk, file_handle, bytes_remaining):
    if(bytes_remaining%100==0):
        print(int(file_handle.tell()*100/(file_handle.tell()+bytes_remaining)),' %')

#playlistLink = input('Enter Playlist Link >>>')

# list = getPlaylistLinks(playlistLink)

# print(len(list))

# for li in list:
#     print('donwloading...........')
#     yt = YouTube(li)
#     print(yt.title)
#     yt.register_on_progress_callback(show_progress)
#     yt.streams.filter(progressive=True, file_extension='mp4',res='360p').order_by('resolution').desc().first().download('/home/jonyroy/ytd')
#     print('download completed.')


def readLine():
    filepath = input('Enter PlayLists File Path: ').strip()
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
        fp.close()
    return lin

allPlayLists = readLine()
print('Total PlayList: ' + str(len(allPlayLists)))

c = 46

videoCounter = 0

for palyList in allPlayLists:
    playListLinks = getPlaylistLinks(palyList)
    numOfVideo = len(playListLinks)
    path_to_save = '/home/jonyroy/ytd/'+ str(c)+'-'+str(numOfVideo)
    os.makedirs(path_to_save,exist_ok=True)

    c = c + 1
    print('Number Of Videos: ' + str(numOfVideo))
    for link in playListLinks:
        try:
            yt = YouTube(link)
            print('downloading........')
            videoCounter = videoCounter + 1
            print(str(videoCounter) + ": " + yt.title)
            yt.streams.filter(progressive=True, file_extension='mp4',res='360p').order_by('resolution').desc().first().download(path_to_save)
            print('download completed.')
        except Exception as e:
            print("Error:")
            print("PlayList:" + palyList)
            print("Video Link: " + link)

print("Total :" + str(videoCounter))