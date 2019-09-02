#! /usr/bin/env python3
from __future__ import print_function
import string

import sys        # command line arguments
import re         # regular expression tools
import os         # checking if file exists
import subprocess # executing program
inputFname = sys.argv[1]
outputFname = sys.argv[2]


text = open(inputFname, 'r')
# Create an empty dictionary
d = dict()

# Asks for file to user and then opens it in read mode
#with open(inputFname, 'r') as searchFile:
    # Loop through each line of the file
for line in text:
    # Remove the leading spaces and newline character
    line = line.strip()
    # Convert the chars to lowercase
    line = line.lower()

    # Removes punctuation
    line = re.sub(r'[^\w\s]','',line)

    # Split line into words
    words = line.split(" ")

    # Loop to iterate through every word in the line
    for word in words:
        # Check if the word is already in dictionary
        if word in d:
            # Increment count of word by 1
            d[word] = d[word] + 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1

# Print the contents of dictionary in descending order by asking for output file to store the words
with open(outputFname, 'w') as f:
    for key in sorted(d.keys()):
        print(key, " ", d[key], file=f)



