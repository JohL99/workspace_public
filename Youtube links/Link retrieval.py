from bs4 import BeautifulSoup
import requests
import pytube

def getPlaylistLinks(filename, url):
    file1 = open(filename,"w+")
    sourceCode = requests.get(url).text
    soup = BeautifulSoup(sourceCode, 'html.parser')
    domain = 'https://www.youtube.com'
    for link in soup.find_all("a", {"dir": "ltr"}):
        href = link.get('href')
        if href.startswith('/watch?'):
            file1.write(link.string.strip() +'\n')
            file1.write(domain + href + '\n')
            file1.write('\n')


def DownloadVids(filename):
    with open(filename) as f:
        if 'https://www.youtube.com/watch?' in f:
            video_url = f.readlines()
            #print(f.readlines())
            #video_url = f.readlines()
            youtube = pytube.YouTube(video_url)
            video = youtube.streams.first()
            video.download('C:\\Users\\toxxi\\Desktop\\python\\Youtube links')



link = input('Playlist to download: ')
getPlaylistLinks('Links.txt', link)
print('Complete')
DownloadVids('Links.txt')
print('Complete2')

