from bs4 import BeautifulSoup
import lxml
import requests
import random
from tkinter import *

# gui information
master = Tk()

# !TODO:requests function should go here

pep8_main = "https://www.python.org/dev/peps/"
pep8_main_requests = requests.get(pep8_main)
pep8_main_raw = pep8_main_requests.content
soup = BeautifulSoup(pep8_main_raw, features="lxml")

# Get Complete List of peps from index
pep_list = [] # initialize blank list

# for each link in our soup find any link with a class of reference external, append to pep_list
for a in soup.findAll('a', class_='reference external'):
    p = a.get_text()
    pep_list.append(p)

# choose a random pep # with random module
random_pep = random.choice(pep_list)

# control statement to add additional 0 to pep number if needed
# website uses a 4 digit code for pep number

if len(random_pep) != 4:
    random_url = pep8_main + "pep-0" + random_pep
else:
    random_url =pep8_main + "pep-" + random_pep

# requests function to grab chosen pep content

pep_url = requests.get(random_url)
pep_url_raw = pep_url.content
pep_soup = BeautifulSoup(pep_url_raw, 'lxml')
# Get Title Of chosen Pep
pep_title = pep_soup.title.get_text()
# Find all body sections
pep_soup_body = pep_soup.find_all(class_='section')
# Create blank list, get only text of section found then append to blank list
pep_section_list = []
for s in pep_soup_body:
    pep_section_list2 = s.get_text()
    pep_section_list.append(pep_section_list2)
pep_section_list3 = ' '.join(str(x) for x in pep_section_list) 

# Create new soup from chosen pep
pep_soup_body = pep_soup.find_all(class_='section')

# create a list & append each 'section' of chosen pep web page body
text_list = []
for s in pep_soup_body:
    text_list_2 = s.get_text()
    text_list.append(text_list_2)
text_list_final = ' '.join(str(x) for x in text_list) 


# Create Scroll Bar
scroll=Scrollbar(master)
scroll.pack(side=RIGHT, fill=Y)

# Create Text Widget for Pep
gui_text = Text(master, wrap=WORD, yscrollcommand=scroll.set, font="Times", width=60, height=30, bd=2, padx=2)
gui_text.configure(background='#306998', foreground='#FFD43B')
gui_text.insert("1.0", text_list_final)
gui_text.pack(side=LEFT, expand=True, fill='both')

# configure scrollbar for text widget
scroll.configure(command=gui_text.yview)

# change title of window to random pep title
master.title(pep_title)

# start main
mainloop()
