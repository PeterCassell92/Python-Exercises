#!usr/bin/python3
from bs4 import BeautifulSoup
import requests

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html)
title = soup.find('title').string

print(title)

for story_heading in soup.find_all('h2'): 
    print(story_heading.string)

        #site-content > div.css-189d5rw.e6b6cmu0 > div.css-11bbiel > div > div.css-717c4s > div > section > div.css-n7jldk > div:nth-child(1) > article > div > a > div > h2

#print(soup.prettify)