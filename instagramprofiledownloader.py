#INSTAGRAM PROFILE DOWNLOADER
#COPY THE PROFILE USERNAME OF ANY PERSON IN INSTAGRAM YU FOLLOW
#PASTE IT IN THE INPUT BOX
#TYPE ENTER
#THE SCRIPT COLLECTS THE LINKS TO ALL POSTS THE PERSON EVER MADE ON INSTAGRAM
#THEN PROCEEDS TO GRAB 'EM ALL
#AUTHOR: CHARLES
import requests
from selenium import webdriver
import os
import time
import re
import sys

regex = re.compile(
        r'^(?:http|ftp)s?://' 
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' 
        r'localhost|' 
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' 
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
count=0
visitedLinkSet={'nothing'}
downloadedImageSet={"nothing"}
downloadedVideoSet={"nothing"}
path=os.path.join("E:/instagram/", "instagram profiles")
try:
    os.mkdir(path)
except OSError as err:
    print(err)
    
username=input("Enter username of the instagram account: ")
path=os.path.join("E:/instagram/instagram profiles/", str(username))
try:
    os.mkdir(path)
except OSError as err:
    print(err)
directory="E:\\instagram\\instagram profiles\\"+str(username)+"\\"

options=webdriver.ChromeOptions()
profilePath="user-data-dir=C:\\Users\\INFO\\AppData\\Local\\Google\\Chrome\\User Data"
options.add_argument(profilePath)
driverPath=r'C:\\Users\\INFO\\Desktop\\Chromedriver'
driver=webdriver.Chrome(options=options, executable_path=driverPath)
driver.get("https://www.instagram.com/"+username+"/")
time.sleep(20)

scrollscript="window.scrollBy(0, 1000)"

#DOWNLOAD IMAGES
def downloadImage(link):
    global count
    filename="instagram" + str(count) + ".jpg"
    count+=1
    print("downloading "+filename)
    if re.match(regex, link) != None:
        r=requests.get(link)
        time.sleep(2)
        if r and r.status_code == 200:
            with open(directory+filename, 'wb') as f:
                for chunk in r.iter_content(1024):
                    if chunk:
                        f.write(chunk)
    return
     
#DOWNLOAD VIDEO                   
def downloadVideo(link):
    global count
    filename="instagram" + str(count) + ".mp4"
    count+=1
    print("downloading " + filename)
    r=requests.get(link, stream=True)
    if r and r.status_code == 200:
        with open(directory+filename, 'wb') as f: 
            for chunk in r.iter_content(chunk_size = 1024*1024): 
                if chunk: 
                    f.write(chunk) 
    return
                
def scroll():
    driver.execute_script(script=scrollscript)
    
#EXTRACT IMAGES AND VIDEOS FROM THE POST PAGE
def extractImages(linkhash):
    postlink="https://www.instagram.com/p/"+linkhash+"/"
    driver.get(postlink)
    time.sleep(5)
    try:
        react=driver.find_element_by_tag_name('svg')
        if react.get_attribute("fill") == "#262626":
            react.click()
    except:
        pass
    try:
        video=driver.find_element_by_tag_name('video')
        videosrc=video.get_property('src')
        if videosrc:
            if videosrc not in downloadedVideoSet:
                downloadedVideoSet.add(videosrc)
                downloadVideo(videosrc)
    except:
        pass
    ul=driver.find_element_by_tag_name('ul')
    images=ul.find_elements_by_class_name("FFVAD")
    if(len(images)>0):
        for image in images:
            imagelink=image.get_property('src')
            if imagelink not in downloadedImageSet:
                downloadImage(imagelink)
                downloadedImageSet.add(imagelink)
    else:
        image=driver.find_element_by_class_name("FFVAD")
        imagelink=image.get_property('src')
        if imagelink not in downloadedImageSet:
            downloadImage(imagelink)
            downloadedImageSet.add(imagelink)
    
    
#GET THE LINKS TO THE POST PAGES
for i in range(200):
    time.sleep(5)
    links=driver.find_elements_by_tag_name('a')
    for link in links:
        href=str(link.get_property('href'))
        if "/p/" in href:
            linkhash=href[len(href)-12:len(href)-1]
            visitedLinkSet.add(linkhash)
    sys.stdout.write("\rCollected " + str(len(visitedLinkSet)) + " links")
    sys.stdout.flush()
    scroll()
    
        
#VISIT ALL POST LINKS AND DOWNLOAD IMAGES
for linkhash in visitedLinkSet.copy():
    if(linkhash != "nothing"):
        extractImages(linkhash)
        visitedLinkSet.remove(linkhash)
        
#dishapatani
#ritabhari_chakraborty
#urvashirautela
#nainaganguly
#sunnyleone
    