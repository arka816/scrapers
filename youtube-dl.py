import pafy
import requests
import os

path=os.path.join("E:/", "Youtube")
try:
    os.mkdir(path)
except OSError as err:
    print(err)
    
directory = "E:\\Youtube\\"
url = input("Enter youtube video url: ")
video = pafy.new(url)
best = video.getbest()
playurl = best.url
print(playurl)

def downloadVideo(link):
    file_name=input("save file as: ")+".mp4"
    print("downloading " + file_name)
    r=requests.get(link, stream=True)
    with open(directory + file_name, 'wb') as f: 
        for chunk in r.iter_content(chunk_size = 1024*1024): 
            if chunk: 
                f.write(chunk) 
                
    return

downloadVideo(playurl)