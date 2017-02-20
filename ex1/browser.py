#!/usr/bin/env python

import urllib
url = "http://studentnet.cs.manchester.ac.uk/ugt/COMP18112/page1.html"
data = urllib.urlopen(url)
tokens = data.read().split()

# loop through pages with links
while True:

    # declare a boolean to enable printing
    printing = False

    # https://www.tutorialspoint.com/python/string_find.htm
    #
    # Used to read about the method find

    for token in tokens:
        if token == '</title>' or token == '</h1>' or token == '</p>' or \
           token == '</em>' or token == '<em>' or token == '<a' or \
           token == '</a>':
            printing = False
        if printing == True:
            print token,
        if token == '<title>':
            print "Page title :",
    	    printing = True
        elif token == '<h1>':
             print "\nHEADING:",
    	     printing = True
        elif token == '<p>':
             print "\nPARAGRAPH:",
    	     printing = True
        elif token == '<em>':
            printing = True
            print '\033[1m',
        elif token == '</em>':
            print '\033[0;0m',
        elif token.find("href") != -1 :
            printing = True

    print "\n"

    # variable used for the list of links
    no = 1
    pages = []
    links = False

    # https://docs.python.org/2/library/functions.html#str
    #
    # Used to serach about casting into a string
    for token in tokens:
        search = token.find('="')
        end = token.find('">')
        if search != -1:
            links = True
            print str(no)  + " :",
            print token[search + 3: end] + "\n"
            pages.append(token[search + 3: end])
            no= no + 1

    # If there aren't any links in the page exit the while loop
    if links == False:
        break

    # take user input
    print "\nIf you want to close the browser select link 0."
    pageNumber = raw_input('Select a link: ')

    # if the user types 0 then exit the browser
    if pageNumber == "0":
        break

    # compute the next link to open based on the user input
    url1 = "http://studentnet.cs.manchester.ac.uk/ugt/COMP18112"
    data = urllib.urlopen(url1 + str(pages[int(pageNumber) - 1]))
    tokens = data.read().split()
