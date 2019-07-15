from bs4 import BeautifulSoup
import lxml
import requests

pep8_main = "https://www.python.org/dev/peps/#finished-peps-done-with-a-stable-interface/"
pep8_main_requests = requests.get(pep8_main)
pep8_main_raw = pep8_main_requests.content

soup = BeautifulSoup(pep8_main_raw, 'lxml')

print(soup.title.get_text())
print(soup.find(class_='text').get_text())
