#! /usr/bin/env python3
# Author: Mahendran
# Description:  This script will demo for exercise fom chapter 4
"""
      Docstring:
"""

#                    1         2         3         4
#          012345678901234567890123456789012345678901234567890
Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

fields = Belgium.split(',')
print('-'*len(Belgium))
print(':'.join(fields))
print(int(fields[1])+int(fields[3]))
print('-'*len(Belgium))