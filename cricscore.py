# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import urllib.request
import requests
from bs4 import BeautifulSoup

url = "http://www.cricbuzz.com/cricket-match/live-scores"
sourcecode = requests.get(url)
soup = BeautifulSoup(sourcecode.text)
for item in soup.select('div .cb-mtch-lst'):
    print("--------------------------------")
    header = item.contents[0].findAll('a')
    print (header[0].text)
    tournament = item.contents[0].findAll('div')
    print(tournament[0].text, tournament[1].text)
    body = item.contents[1].findAll('div')
    print(body[0].text)
    print(body[1].text)
    print("--------------------------------")
