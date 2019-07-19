from bs4 import BeautifulSoup
import lxml
import requests
import random
import tkinter as Tk

#gui information
window =Tk.Tk()
window.title("Pep-A-Day")


pep8_main = "https://www.python.org/dev/peps/"
pep8_main_requests = requests.get(pep8_main)
pep8_main_raw = pep8_main_requests.content

soup = BeautifulSoup(pep8_main_raw, 'lxml')

#Get Title Of Pep
pep_title = soup.title.get_text()

###Get Complete List of peps from index###
pep_list = [] # initialize blank list

#for each link in our soup find any link with a class of refrence external, append to pep_list
for a in soup.findAll('a', class_='reference external'):
    p = a.get_text()
    pep_list.append(p)

#random pep choice
random_pep = random.choice(pep_list)

#control statement to add additional 0 to pep number if needed
#website uses a 4 digit code for pep number

if len(random_pep) != 4:
    random_url = pep8_main + "pep-0" + random_pep
else:
    random_url =pep8_main + "pep-" + random_pep

#requests function to grab random pep content
pep_url = requests.get(random_url)
pep_url_raw = pep_url.content
pep_soup = BeautifulSoup(pep_url_raw, 'lxml')
pep_soup_text = str(pep_soup.get_text())
#find all items with class 'text' and remove markup
s=Tk.Scrollbar(window)
s.pack(side ='right', fill = 'y')
text= Tk.Text(window, wrap='word').pack(side='left', fill='both', expand='yes')
text.config(yscrollcommand=s.set)
s.config(command=text.yview)
text.insert(Tk.END, pep_soup_text)
window.mainloop()