import requests
import urllib.request
from bs4 import BeautifulSoup

def makeurl(name):
    url = "http://www.shabdkosh.com/hi/translate?e="+name.lower()+"&l=hi"
    return url

def make_soup(url):
    source_code = requests.get(url)
    soup = BeautifulSoup(source_code.text)
    return soup

def writedictionary(url):
    soup = make_soup(url)
    for tags in soup.select('.eirol li a'):
        string = tags.text 
        print(string)
    

word = input('Enter the word?\n')
writedictionary(makeurl(word))
