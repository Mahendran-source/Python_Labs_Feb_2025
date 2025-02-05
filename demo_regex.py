#! /usr/bin/env python3
# Author: Mahendran
# Description: This is demo HOWTO

import re

# open the files handle for reading in Text mode.
fh_in = open(r"c:\labs\words", mode="rt")

# Iterate through files handle one line at a time.
for line in fh_in:
    # Example of str testing = GOOD
    #if line.startswith("Y") and line.rstrip("\n").endswith("n") and "town" in line:
    # m = re.search("^the", line) # Match lines starting with 'the'
    # m = re.search("ing$", line) # Match lines ending with 'ing'
    # m = re.search("^ring$", line) # Match lines with 'ring'
    # m = re.search("^.ing$", line) # Match lines with with 4 char ending with 'ing'
    # m = re.search("^[adr]ing$", line) # Match lines with [adr] followed 'ing'
    # m = re.search("[aeiou][aeiou][aeiou]", line) # Match three continues vowls in a line.
    # m = re.search("[.]", line) # Match lines with a DOT.
    # m = re.search("^[A-Z].*[A-Z]$", line) # Match lines start/end with a Capital
    # m = re.search("^[A-Z].{4}[A-Z]$", line) # Match lines of 6 char start/end with a Capital
    # m = re.search(r"^(.)(.).(\2)(\1)$", line) # Match with palindromes
    m = re.search(r"^([A-Z]).*(\1)$", line) # Match start and ending with same letter.
    if m:
        print(line,end="")

