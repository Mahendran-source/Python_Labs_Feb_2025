#! /usr/bin/env python3
# Author: Mahendran
# Description:  This script will demo how to check which platform
# your script is running on
"""
      Docstring:
"""

import sys
import os

if sys.platform == "win32":
    home_dir = os.environ["HOMEPATH"]
else:
    home_dir = os.environ["HOME"]

print("Printing home dir :", home_dir)
