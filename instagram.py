#INSTAGRAM FEED DOWNLOADER
#AUTHOR: CHARLES
import requests
from selenium import webdriver
import os
import time
import datetime

downloadedImageSet={"nothing"}
path=os.path.join("E:/", "instagram")
badchars=[" ", ":"]
try:
    os.mkdir(path)
except OSError as err:
    print(err)
    
timestring=datetime.datetime.now()
timestring=timestring.strftime("%c")
for i in badchars:
    timestring=timestring.replace(i, "_")
path=os.path.join("E:/instagram/", str(timestring))
try:
    os.mkdir(path)
except OSError as err:
    print(err)
directory="E:\\instagram\\"+str(timestring)+"\\"

options=webdriver.ChromeOptions()
profilePath="user-data-dir=C:\\Users\\INFO\\AppData\\Local\\Google\\Chrome\\User Data"
options.add_argument(profilePath)
driverPath=r'C:\\Users\\INFO\\Desktop\\Chromedriver'
driver=webdriver.Chrome(options=options, executable_path=driverPath)
driver.get("https://www.instagram.com/")
time.sleep(10)

scrollscript="window.scrollBy(0, window.innerHeight*2)"

def downloadImage(link, count):
    filename="instagram" + str(count) + ".jpg"
    print("downloading "+filename)
    r=requests.get(link)
    if r.status_code == 200:
        with open(directory+filename, 'wb') as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)
                
def scroll():
    driver.execute_script(script=scrollscript)

count = 1
for i in range(300):
    time.sleep(5)
    images=driver.find_elements_by_class_name("FFVAD")
    for image in images:
        link=image.get_property('src')
        if link not in downloadedImageSet:
            downloadImage(link, count)
            downloadedImageSet.add(link)
            count+=1
    scroll()
    