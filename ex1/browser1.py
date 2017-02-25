#!/usr/bin/env python
#https://www.tutorialspoint.com/python/python_gui_programming.htm
#
# Used this site to learn about Tkinter
#------------------------------------------------------------------------------
# https://docs.python.org/2/library/functions.html#str
#
# Used to serach about casting into a string
#-----------------------------------------------------------------------------
import urllib
import Tkinter
from Tkinter import *
import tkMessageBox

#Create the window
top = Tkinter.Tk()
# Add a text box to the gui
text = Text(top)

# The first page opened
url = "http://studentnet.cs.manchester.ac.uk/ugt/COMP18112/page3.html"
# The root page for all the other pages
url1 = "http://studentnet.cs.manchester.ac.uk/ugt/COMP18112"
data = urllib.urlopen(url)
tokens = data.read().split()
# Store the links found on a page
pages = []

#Code to read the html page
def print_next_page(tokens):
    pageNumber = ""
    printing = False
    for token in tokens:
        if token == '</title>' or token == '</h1>' or token == '</p>' or \
                token == '</em>' or token == '<em>' or token == '<a' or \
                token == '</a>':
            printing = False
        if printing == True:
            text.insert(INSERT,token + " ")
        if token == '<title>':
            text.insert(INSERT,"Page title :")
    	    printing = True
        elif token == '<h1>':
             text.insert(INSERT, "\nHEADING:")
    	     printing = True
        elif token == '<p>':
             text.insert(INSERT, "\nPARAGRAPH:")
    	     printing = True
        elif token == '<em>':
            printing = True
            print '\033[1m',
        elif token == '</em>':
            print '\033[0;0m',
        elif token.find("href") != -1 :
            printing = True
    text.insert(INSERT,"\n")

    # Index to acces the list with web pages
    no = 1
    #Find the links in the page
    for token in tokens:
        search = token.find('="')
        end = token.find('">')
        if search != -1:
            links = True
            text.insert(INSERT, str(no) + " :" + token[search + 3: end] + "\n")
            pages.append(token[search + 3: end])
            no= no + 1
    #Configure the text box so that it can't be edited
    text.config(state = DISABLED)
    #text.grid(row = 0)
    text.pack(side = TOP)

#Call this function to print the first page
print_next_page(tokens)

l1 = Label(top, text = "Select a link: ")
l1.pack(side = LEFT)

e1 = Entry(top,bd = 5)
e1.pack(side = LEFT)

# Command for the button
def open_link():
    #Get the user input
    pageNumber = e1.get()
    if pageNumber == "1" or pageNumber == "2":
        text.config(state=NORMAL)
        text.delete("1.0",END)
        # open the next page based on the input
        data = urllib.urlopen(url1 + pages[int(pageNumber) - 1])
        del pages[:]
        e1.delete(0,END)
        tokens = data.read().split()
        # print the next page
        print_next_page(tokens)
    else:
        e1.delete(0,END)

#Add the button
b1 =Button(top, text='Open', command=open_link)
b1.pack(side = LEFT)

top.mainloop()
