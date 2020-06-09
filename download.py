#PYTHON BOT FOR DOWNLOADING FILES FROM AZNUDE
import requests
from bs4 import BeautifulSoup
import os

path=os.path.join("E:/", "Erotic")
try:
    os.mkdir(path)
except OSError as err:
    print(err)

name = input("Enter name: ")
surname = input("Enter surname: ")
path=os.path.join("E:/Erotic/", name + " " + surname)
try:
    os.mkdir(path)
except OSError as err:
    print(err)
    
directory = "E:\\Erotic\\" + name + " " + surname

URL = "https://search.aznude.com/?q=" + name + "+" + surname +"&t=f&submitBtnAZN=Search"
r=requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
divs=soup.findAll('div', attrs={'class': 'movie'})

def downloadVideo(link):
    link=link.replace('largeCelebPage-4.jpg', 'hd.mp4')
    link = "https:" + link
    file_name = link.split("/")[-1]
    print("downloading " + file_name)
    r=requests.get(link, stream=True)
    with open(directory + "\\" + file_name, 'wb') as f: 
        for chunk in r.iter_content(chunk_size = 1024*1024): 
            if chunk: 
                f.write(chunk) 
                
    return
    
for div in divs:
    image = div.find('img', attrs={'alt' : ''})
    if(image['src'] != None):
        downloadVideo(image['src'])