#SCRIPT FOR DOWNLOADING FILES FROM XNXX
#NEEDS CHROMEDRIVER FOR SELENIUM INSTALLED
#NEEDS BEAUTIFUL SOUP AND SELENIUM PYTHON MODULES INSTALLED
#AUTHOR: ARKA

import math
import requests
from bs4 import BeautifulSoup
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys

options = Options()
options.add_argument('--headless')
options.add_argument('--profile-directory=Default') 
driverPath=r'C:\\Users\\INFO\\Desktop\\Chromedriver'
driver=webdriver.Chrome(options=options, executable_path=driverPath)
path=os.path.join("E:/", "xnxx")
try:
    os.mkdir(path)
except OSError as err:
    print(err)
        
name=input("Enter name: ")
surname=input("Enter surname: ")
path=os.path.join("E:/xnxx/", name + " " + surname)
try:
    os.mkdir(path)
except OSError as err:
    print(err)
directory="E:\\xnxx\\" + name+ " "+surname+"\\"
searchPageUrl="https://www.xnxx.com/search/" + name + "+" + surname
searchPageRes=requests.get(searchPageUrl)
searchSoup=BeautifulSoup(searchPageRes.content, 'html5lib')
divs=searchSoup.findAll('div', attrs={'class':'thumb-block'})


def downloadVideo(link, count):
    file_name=name+" " + surname + " " + str(count) + ".mp4"
    print("downloading " + file_name)
    r=requests.get(link, stream=True)
    fileSize=math.ceil(int(r.headers['Content-length'])/1024)
    print("file size: " + str(fileSize) + "KB")
    percent=0
    with open(directory + file_name, 'wb') as f: 
        for chunk in r.iter_content(chunk_size = 1024*1024): 
            if chunk: 
                f.write(chunk) 
                percent+=(102400/fileSize)
                string="\rDownloaded: " + str(math.ceil(percent)) + "%"
                if(percent <= 100):
                    sys.stdout.write(string)
                    sys.stdout.flush()
                else:
                    sys.stdout.write("\rDownloaded: 100%")
                    sys.stdout.flush()
    sys.stdout.write("\rDownloaded: 100%")
    sys.stdout.flush()            
    print("\n")
    return

count=1
for div in divs:
    link=div.find('a')
    href=link['href']
    url="https://xnxx.com" + href
    driver.get(url)
    time.sleep(10)
    try:
        div=driver.find_element_by_class_name("video-bg-pic")
    except:
        div=driver.find_element_by_class_name("video-bg-pic")
    video=div.find_element_by_tag_name('video')
    downloadVideo(video.get_property('src'), count)
    count+=1
    