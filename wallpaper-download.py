'''

Made By : Ashutosh Maheshwari
Wallpaper Download Python Script

'''

import requests
import urllib.request
from bs4 import BeautifulSoup

def makeurl(name):
    '''Make the url of the page from search query'''
    title = '-'.join(x.strip() for x in name.split(" "))
    url = "http://www.santabanta.com/wallpapers/"+title.lower()+"/"
    return url

def make_soup(url):
    '''Make Beautiful Soup of the given URL'''
    source_code = requests.get(url)
    soup = BeautifulSoup(source_code.text)
    return soup

def download(url,name):
    ''' Find all the images of the webpage and download it'''
    soup = make_soup(url)
    images = []
    for tags in soup.select('.wallpapers-box-300x180-2-img > a'):
        images.append(tags.attrs['href'])
    print(images)
    for i in range(len(images)):
        fileaddress = "http://www.santabanta.com"+images[i]
        soup_inner = make_soup(fileaddress)
        for dwnld in soup_inner.select('a #wall'):
            urllib.request.urlretrieve(dwnld.attrs['src'],name+" "+str(i)+".jpg")

search = input('Enter the celeb name?  ')
url = makeurl(search)
download(url,search)
