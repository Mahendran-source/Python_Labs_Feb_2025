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
    m = re.search("^ring$", line)
    if m:
        print(line,end="")

