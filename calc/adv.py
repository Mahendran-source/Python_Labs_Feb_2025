#! /usr/bin/env python3
# Author: Mahendran
# Description: This is demo HOWTO

import sys

def mod(x, z):
    """ """
    return x % z

def power(x, z):
    return x**z

def sqrt(x):
    return round(x**0.5, 2)

print(" Advanced Calculator App")
print("-" * 32)

print(f"100 % 30 = {mod(100,30)}")
print(f"100 ** 3 = {power(100,3)}")
print(f"\N{square root}100  = {sqrt(100)}")

sys.exit(0)
