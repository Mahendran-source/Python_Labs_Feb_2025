#! /usr/bin/env python3
# Author: Mahendran
# Description:  This script will demo HOWTO format strings using
# str concatenation and escape chars, str justification methods.
"""
      Docstring:
"""

planets = {'Mercury': 57.91,
           'Venus': 108.2,
           'Earth': 149.597870,
           'Mars': 227.94
}

for planet in planets.key():
    print("\t\t" + planet + ": " + str)