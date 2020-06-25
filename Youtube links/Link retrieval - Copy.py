'''import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))'''

import pytube


video_url = 'https://www.youtube.com/watch?v=KUc9KJrTvUY' # paste here your Youube videos' url
youtube = pytube.YouTube(video_url)
video = youtube.streams.first()
video.download('C:\\Users\\toxxi\\Desktop\\python\\Youtube links') # path, where to video download.'''


