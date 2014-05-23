
#-------------------------------------------------------------------------------
# Name:        lyrics-downloader2.0
# Purpose: creates a text file of the lyrics of a song
#
# Author:      Vijetha PV
#
# Created:
# Copyright:   (c) hp
# Licence:     
#-------------------------------------------------------------------------------

import urllib
import re
import sys,os,inspect
from BeautifulSoup import BeautifulSoup
import eyed3
from eyed3 import mp3
path= sys.argv[1]
audiofile = eyed3.core.load(path)
artist=str(audiofile.tag.artist).lower()
s=str(audiofile.tag.title).lower()
album=str(audiofile.tag.album).lower()
path = path.replace('.mp3',"")
s =s.replace(" ","")
artist= artist.replace(" ","")
album=artist.replace(" ","")
if 'http://www.azlyrics.com/lyrics/'+artist+'/'+ s+'.html':
    url='http://www.azlyrics.com/lyrics/'+artist+'/'+ s+'.html'
else if:'http://www.azlyrics.com/lyrics/'+artist+'/'+album+'.html'
    url='http://www.azlyrics.com/lyrics/'+artist+'/'+ album+'.html'

htmltext = urllib.urlopen(url).read()
soup =BeautifulSoup(htmltext)

products= soup.findAll("div", style = "margin-left:10px;margin-right:10px;")

lyrics= " ".join(str(x) for x in products)
takeoff=['<br />','</div>','<i>','</i>','<div style="margin-left:10px;margin-right:10px;">']
for j in takeoff:
    lyrics=lyrics.replace(j,"\n")
print lyrics
with open (path+".txt","wb") as l:
    l.write(lyrics)
l.close()
