#! /usr/bin/env python3
# Author: Mahendran
# Description: This is demo HOWTO


import re
import sys

if sys.platform=='win32':
    file=r"c:\windows\system32\drivers\etc\services"
else:
    file='/etc/service'

ports = set()

for line in open(file,'r'):
    m=re.search(r"(\d+)/(udp|tcp)", line)
    if m:
        port = int(m.group(1))
        if port > 200: break
        ports.add(port)

print(set(range(1,201))- ports)