#!usr/bin/python3

#This program takes all the text from an article across two pages and writes the text to a file.
import requests
from bs4 import BeautifulSoup

def print_webpage_text(base_url):
	r = requests.get(base_url)
	soup = BeautifulSoup(r.text, "html.parser")
	title = soup.find('title').string

	
	for text in soup.find_all('p'):
	    with open('ex21savefile.txt', 'a') as open_file:
   			open_file.write(text.get_text())
	print("Writing Complete")

base_url1 = 'http://www.washingtonpost.com/wp-dyn/content/article/2010/08/29/AR2010082902749.html'
base_url2 = 'http://www.washingtonpost.com/wp-dyn/content/article/2010/08/29/AR2010082902749_2.html?sid=ST2010082902923'

urls = [base_url1, base_url2]
for url in urls:
	print_webpage_text(url)