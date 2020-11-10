import requests
from bs4 import BeautifulSoup
import os
import random
import json
import time
import re
import codecs
from math import ceil

def findAllHyperlink(loader, url):
    strHtml = loader.getHTML(url)
    if len(strHtml) == 0:
        return []

    # print(url)
    # print(strHtml)
    soup = BeautifulSoup(strHtml, 'lxml')
    absolutes = soup.find_all('a',attrs={'href': re.compile("^https://www.fst.um.edu.mo.*")})
    relatives = soup.find_all('a',attrs={'href': re.compile(".*/.*")})

    absoluteHyperlinks = [abso.attrs['href'] for abso in absolutes]
    relativeHyperlinks = [rela.attrs['href'] for rela in relatives]
    for rela in relativeHyperlinks:
        if rela.find('http') != -1:
            continue
        else:
            absoluteHyperlinks.append('https://www.fst.um.edu.mo' + rela)
    return absoluteHyperlinks

class HTMLoader:
    def __init__(self):
        self.reTryCnt = 0
        self.maxReTryCnt = 3
        with open('proxies.json','r') as f:
            self.proxies = json.load(f)

    def getHTML(self, url, ifProxy=0):
        # print(url)
        # print('downloading...')
        while True:
            # time.sleep(random.random() * 0.5)
            proxy = random.choice(self.proxies)
            try:
                if ifProxy:
                    strhtml = requests.get(url, timeout=30, proxies=proxy)
                else:
                    strhtml = requests.get(url, timeout=30)
                # print(url)
                # print(200)
                return strhtml.text
            except:
                # print(url)
                print('fail, and try again.')
                self.reTryCnt += 1
                if self.reTryCnt == self.maxReTryCnt:
                    self.reTryCnt = 0
                    return ''
