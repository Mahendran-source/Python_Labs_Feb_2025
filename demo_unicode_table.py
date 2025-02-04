#! /usr/bin/env python3
# Author: Mahendran
# Description:  This script will demo howto display the entire
# UNICODE char set
"""
      Docstring:
"""



for pos in range(0,65535):
    try:
        print(char(pos), end=" ")
        if pos % 16 ==0:
            print()
    except UnicodeError:
        print(" ",end=" ")


