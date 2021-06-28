#!/bin/env python3.8


from subprocess import Popen, PIPE

import sys
import json

result = {}
result['all'] = {}


pipe = Popen(['getent', 'hosts'], stdout=PIPE, universal_newlines=True)

result['all']['hosts'] = []

for line in pipe.stdout.readlines():
    s = line.split()
    result['all']['hosts'].append(s[1])

print(result)

