#! /usr/bin/env python3
# Author: Mahendran
# Description:  This script will simulate a high stree bank
# ATM PIN machine.
"""
      Docstring:
"""

master_pin = "0123"
pin = None
attempts = 0

# Loop whilst PIN is incorrect
while pin != master_pin and attempts < 3:
    pin = input("Enter PIN: ")
    if pin == master_pin:
        print("Valid PIN")
    else:
        print("Ïnvalid PIN")
        attempts += 1

print("Done.")