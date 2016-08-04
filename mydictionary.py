'''
Made by Ashutosh Maheshwari
My Dictionary from thefreedictionary.com
'''

import requests
from bs4 import BeautifulSoup

def makeurl(word):
    url = "http://www.thefreedictionary.com/"+word
    return url

def makesoup(url):
    source_code = requests.get(url)
    soup = BeautifulSoup(source_code.text)
    return soup

def writedict(url):
    soup = makesoup(url)
    for tags in soup.select('div .pseg'):
        string = tags.text
        print(string.split('\n'))
        File.write(word+"\n")
        File.write(str(string.split('\n')))
        File.write("\n")


word = input('Enter the word?\n')
File = open('mydictionary.txt','a')
writedict(makeurl(word))

