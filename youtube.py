import requests

directory = "E:\\Erotic\\"
video_id="Iwo4YXFby4c"
URL="https://www.youtube.com/get_video_info?video_id=" + video_id + "&el=detailpage&ps=default&eurl="
r=requests.get(URL)

url1="https://www.youtube.com/get_video_info?&video_id=Iwo4YXFby4c"
r1=requests.get(url1)
url2="http://www.youtube.com/get_video?video_id=Iwo4YXFby4c&t=AB9zfpLPJ2AtQrkp4pCdrGhfDeEErNKVhuzJKRCwjQq2qnh83yCfeSWpKh_s8Ilc-R2VwMZeOdyIKkfU3amhC1PurN1LhvtqPs1YKXMIpfDnIue_XWgl_dF4mfPzQhvnIEh94J5_avqysPv4-GsilXc0kUZNNZ7OPA"
r2=requests.get(url2)

def extractRawUrl(content):
    content = str(content)
    res=[i for i in range(len(content)) if content.startswith('https', i)]
    for i in range(len(res)-1):
        rawString=content[res[i]:res[i+1]]
        if "googlevideo.com" in rawString:
            return rawString
        
        
def parseUrl(url):
    while(url.find("%") != -1):
        pos=url.find("%")
        code=url[(pos+1):(pos+3)]
        codeInt=int(code, 16)
        string=str(chr(codeInt))
        url=url[:pos] + string + url[pos+3:]
    return url

def downloadVideo(link):
    file_name = "my file.mp4"
    print("downloading " + file_name)
    r=requests.get(link, stream=True)
    with open(directory + file_name, 'wb') as f: 
        for chunk in r.iter_content(chunk_size = 1024*1024): 
            if chunk: 
                f.write(chunk) 
                
    return

    
rawUrl=extractRawUrl(r.content)
parsedUrl = parseUrl(rawUrl)
print(parsedUrl)
downloadVideo(parsedUrl)

print(parseUrl(str(r1.content)))
