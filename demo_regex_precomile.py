#! /usr/bin/env python3
# Author: Mahendran
# Description: This is demo HOWTO

import re

# open the files handle for reading in Text mode.
fh_in = open(r"c:\labs\words", mode="rt")

# Iterate through files handle one line at a time.
for line in fh_in:
   m = re.search(r"^([A-Z]).*(\1)$", line) # Match start and ending with same letter.
    if m:
        print(line,end="")
