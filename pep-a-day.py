from bs4 import BeautifulSoup
import lxml
import requests
import random
from tkinter import *

# gui information
master = Tk()

# function to convert requests to bs4 soup


def requests_bs4_convert(url):
    request_url = requests.get(url)
    request_return_raw = request_url.content
    request_soup_convert = BeautifulSoup(request_return_raw, features="lxml")
    return request_soup_convert


# Stage 1 - finding and choosing our random pep


pep8_main = "https://www.python.org/dev/peps/"
main_soup = requests_bs4_convert(pep8_main)
# Get Complete List of peps from index
pep_list = []  # initialize blank list

# for each link in our soup find any link with a class of reference external, append to pep_list
for a in main_soup.findAll('a', class_='reference external'):
    p = a.get_text()
    pep_list.append(p)

# choose a random pep # with random module from our previously generated pep_list
random_pep = random.choice(pep_list)

# control statement to add additional 0 to pep number if needed
# website uses a 4 digit code for pep number

if len(random_pep) != 4:
    random_url = pep8_main + "pep-0" + random_pep
else:
    random_url = pep8_main + "pep-" + random_pep

# requests function to grab  randomly chosen pep content

random_pep_soup = requests_bs4_convert(random_url)

# Get Title Of chosen Pep
random_pep_title = random_pep_soup.title.get_text()

# Find body section
pep_soup_body = random_pep_soup.find_all(class_='section')

# Create blank list, get only text of section found then append to blank list
pep_section_list = []
for s in pep_soup_body:
    pep_section_list2 = s.get_text()
    pep_section_list.append(pep_section_list2)
pep_section_list3 = ' '.join(str(x) for x in pep_section_list)

# Create new soup from chosen pep
pep_soup_body = random_pep_soup.find_all(class_='section')

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
master.title(random_pep_title)

# start main
mainloop()
