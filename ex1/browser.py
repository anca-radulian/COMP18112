#!/usr/bin/env python

import urllib

url = "http://studentnet.cs.manchester.ac.uk/ugt/COMP18112/page3.html"
data = urllib.urlopen(url)
tokens = data.read().split()

# declare a boolean to enable printing
printing = False

# print the
print "Page title :",
for token in tokens:
    if printing == True:
	    if not (token == '</title>'):
    	       print token,
    if token == '<title>':
    	printing = True
    if token == '</title>':
    	printing = False

# print the text inside the <h1> tags

print "\nHEADING:",
for token in tokens:
    if printing == True:
	    if not (token == '</h1>'):
    	       print token,
    if token == '<h1>':
    	printing = True
    if token == '</h1>':
    	printing = False

# print the text inside <p> tags and emphasise the text between <em> tags

for token in tokens:
    if printing == True:
	    if not (token == '</p>' or token == '<em>' or token == '</em>'/
                token == '<a>' or token == '</a>'):
    	       print token,
    if token == '<p>':
    	printing = True
        print "\nPARAGRAPH:",
    if token == '<em>' or token =='</em>':
        print '\033[1m',
    if token == '</em>':
        print '\033[0;0m',
    if token == '</p>':
    	printing = False
