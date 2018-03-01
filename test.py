from bs4 import BeautifulSoup
import requests
# url = "https://www.youtube.com/watch?v=q5BGs_ipzSg&list=PL1pf33qWCkmibUP3X3Xah-vGZk0MLhu-B"
url = "https://www.youtube.com/playlist?list=PL1pf33qWCkmjXSs_H2VcCEGsT6SilT1TT"
try:
    sourceCode = requests.get(url).text
    soup = BeautifulSoup(sourceCode, 'html.parser')
    domain = 'https://www.youtube.com'
    for link in soup.find_all("a", {"dir": "ltr"}):
        href = link.get('href')
        if href.startswith('/watch?'):
            #print()
            #print(link.string.strip())
            print(href)
                
except Exception as e:
    print("Request Error: " + url)

# def readLine():
#     filepath = 'link.txt' 
#     lin = [] 
#     with open(filepath) as fp:  
#         line = fp.readline()
#         #print(line)
#         cnt = 1
#         while line:
#             l = line.strip()
#             if(len(l)>0):
#                 lin.append(l)
#                 #print(line.strip())
#             #print("Line {}: {}".format(cnt, line.strip()))
#             line = fp.readline()
#             cnt += 1
#         fp.close()
#     return lin

# allPlayLists = readLine()
# print('Total PlayList: ' + str(len(allPlayLists)))