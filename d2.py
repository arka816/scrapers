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

playScript= "document.getElementsByTagName(\"video\")[0].play()"
pauseScript="document.getElementsByTagName(\"video\")[0].pause()"


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


count = 1
for li in lis[:2]:
    videoPageUrl="https://www.pornhub.org/view_video.php?viewkey=" + li['_vkey']
    driver.get(videoPageUrl)
    time.sleep(10)
    try:
        sources=driver.find_elements_by_tag_name('source')
    except:
        sources=driver.find_elements_by_tag_name('source')
    for source in sources:
        if(source.get_property("type") == "video/mp4"):
            src=source.get_property("src")
            driver.execute_script(playScript)
            while("phncdn.com" not in src):
                src=source.get_property("src")
                time.sleep(5)
                driver.execute_script(pauseScript)
                driver.execute_script(playScript)
                print("waiting...")
            downloadVideo(src, count)
            count+=1
            
            
            
                
                    
        
        
        