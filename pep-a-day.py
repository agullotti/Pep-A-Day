from bs4 import BeautifulSoup
import lxml
import requests
import random

pep8_main = "https://www.python.org/dev/peps/"
pep8_main_requests = requests.get(pep8_main)
pep8_main_raw = pep8_main_requests.content

soup = BeautifulSoup(pep8_main_raw, 'lxml')

#Get Title Of Pep
print(soup.title.get_text())

###Get Complete List of peps from index###
pep_list = [] # initialize blank list

#for each link in our soup find any link with a class of refrence external
for a in soup.findAll('a', class_='reference external'):
    p = a.get_text()
    pep_list.append(p)
print(pep_list)