#!/usr/bin/env python3.4

import time, os

i = 0
c = 1
SIZE = 100
while True:
    i += c
    if i > SIZE:
        c = -c
        i = SIZE
    elif i < 0:
        c = -c
        i = 0
    # os.system("clear")
    print('\r', ' ' * i, '-', ' '*(SIZE-i))
    time.sleep(0.1)
