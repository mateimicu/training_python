#!/usr/bin/env python3.4

import sys

with open("text.txt", "r") as fin:
    for line in fin:
        if line.strip() not in sys.argv :
            print(line, end='')
