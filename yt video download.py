#pip install yt-dlp --> first import pip using cmd
import yt_dlp
url= input ("Enter video url:")
ydl_opts = {}
with yt_dlp.YoutubeDL(ydl_opts)as ydl:
    ydl.download([url])
    print("video download successfully")

    #souce code --> https://www.clcoding.com/

