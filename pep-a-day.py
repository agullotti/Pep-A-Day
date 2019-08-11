# Imports needed
from bs4 import BeautifulSoup  # Needed for creating formatted text from web page
import lxml  # Needed to parse html with bs4
import requests  # Needed for requesting content from web page
import random  # Needed for random choice
from tkinter import *  # Needed for GUI
import sys  # Needed for program restart
import os  # Needed for program restart

#######################################################################

# initialize tkinter
master = Tk()

# function to convert requests to bs4 soup
def requests_bs4_convert(url):
    request_url = requests.get(url)
    request_return_raw = request_url.content
    request_soup_convert = BeautifulSoup(request_return_raw, features="lxml")
    return request_soup_convert


# function to restart program
def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


#######################################################################

# go to pep index->turn index into soup for parsing
peps_main = "https://www.python.org/dev/peps/"
main_soup = requests_bs4_convert(peps_main)

#######################################################################

# for each link in our index soup find any link with a class of reference external, append to pep_list as text
pep_list = []  # initialize blank list
for a in main_soup.findAll('a', class_='reference external'):
    p = a.get_text()
    pep_list.append(p)

#######################################################################

# choose a random pep # with random module from our previously generated pep_list
random_pep = random.choice(pep_list)
# control statement to add additional 0 to pep number if needed
# website uses a 4 digit code for pep number link but displays as a 3 digit
if len(random_pep) != 4:
    random_url = peps_main + "pep-0" + random_pep
else:
    random_url = peps_main + "pep-" + random_pep

#######################################################################

# requests function to grab  randomly chosen pep content
random_pep_soup = requests_bs4_convert(random_url)
# Get Title Of chosen Pep
random_pep_title = random_pep_soup.title.get_text()

#######################################################################

# Create blank list for each page section found
text_list = []
# Find all class 'section' for needed content
pep_soup_body = random_pep_soup.find_all(class_='section')
# For each 'section' found, get only it's text, append to a list, then convert list to string
for s in pep_soup_body:
    text_list_2 = s.get_text()
    text_list.append(text_list_2)
text_list_final = ' '.join(str(x) for x in text_list)

#######################################################################
# Tkinter configuration begin
#######################################################################

# create restart button
restart_button = Button(master, text='Again?', command=restart_program).pack(fill=Y)
# Create Scroll Bar
scroll = Scrollbar(master)
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
