#! /usr/bin/env python3
# Author: Mahendran
# Description: This is demo HOWTO

def frange(start, stop, step=0.25):
    val=float(start)
    while val < stop:
        yield val
        val+=step

print(list(frange(1.1,3)))
print(list(frange(1,3,0.33)))
print(list(frange(1,3,1)))
print(list(frange(1,3,0.5)))
print(list(frange(-1,-0.5,0.1)))

for num in frange(3.142,12):
    print(f"{num:05.2f}")

