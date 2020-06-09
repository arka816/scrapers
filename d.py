import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os

driverPath=r'C:\\Users\\INFO\\Desktop\\Chromedriver'
driver=webdriver.Chrome(executable_path=driverPath)
path=os.path.join("E:/", "Erotic")
try:
    os.mkdir(path)
except OSError as err:
    print(err)
directory = "E:\\Erotic\\"
name='Monica'
surname='Bellucci'
searchPageUrl = "https://www.pornhub.org/video/search?search="+name+"+"+surname
searchPageReq=requests.get(searchPageUrl)
searchPageContent=searchPageReq.content
searchSoup=BeautifulSoup(searchPageContent, 'html5lib')
ul=searchSoup.find("ul", attrs={'id':'videoSearchResult'})
lis=ul.findAll('li', attrs={'class':'pcVideoListItem'})

def downloadVideo(link, count):
    print(link)
    file_name=name+surname+str(count)+".mp4"
    print("downloading " + file_name)
    r=requests.get(link, stream=True)
    with open(directory+file_name, 'wb') as f: 
        for chunk in r.iter_content(chunk_size = 1024*1024): 
            if chunk: 
                f.write(chunk) 
    return

def refresh(playButtons):
    for playButton in playButtons:
        playButton.click()

count = 1
for li in lis[:2]:
    videoPageUrl="https://www.pornhub.org/view_video.php?viewkey=" + li['_vkey']
    driver.get(videoPageUrl)
    time.sleep(10)
    playButtons=driver.find_elements_by_class_name("mhp1138_playerStateIcon")
    refresh(playButtons)
    time.sleep(2)
    try:
        sources=driver.find_elements_by_tag_name('source')
    except:
        sources=driver.find_elements_by_tag_name('source')
    for source in sources:
        if(source.get_property("type") == "video/mp4"):
            src=source.get_property("src")
            while('phncdn.com' not in src):
                time.sleep(5);
                refresh(playButtons)
            downloadVideo(src, count)
            count+=1
        
        
        
        