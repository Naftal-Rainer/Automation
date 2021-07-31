from __future__ import unicode_literals
import youtube_dl
import urllib
import shutil

url = 'https://www.youtube.com/watch?v=n06H7OcPd-g'

ydl_opts = {}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])