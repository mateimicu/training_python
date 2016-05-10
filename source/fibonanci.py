#!/usr/bin/env python3.4

import sys
"""
Scrieti o functie care primeste un rang si returneaza al rang-ulea numar din sirul fib...
1 1 2 3 5 8 ...
"""

# l = [1, 1]
# l = {0: 1, 1:1}

def fib(a):
    # if a <= 2:
    #     return 1
    # else:
    #     return fib(a-1) + fib(a-2)
    # for i in range(2, a):
    #     # l.append(l[i-2] + l[i-1])
    #     l[i] = l[i-1] + l[i-2]
    # return l[a-1]
    s1 = 1
    s2 = 1
    for i in range(2, a):
        s1, s2 = s2, s1+s2
    return s2


try:
    print(fib(int(sys.argv[1])))
except :
    print("Stuff !")
