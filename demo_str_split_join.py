#! /usr/bin/env python3
# Author: Mahendran
# Description:  This script will demo HOWTO split and rejoin strings
# using the .split() and .join() methods
"""
      Docstring:
"""

line = "root:x:0:0:The Super User:/root:/bin/ksh"

# AND I want to Modify the string! But str are IMMUTABLE!

fields = line.split(":")
fields[4] = "The Administrator"
fields[6] = "/bin/bash"
line = ":".join(fields)

print(fields)

print(line)
