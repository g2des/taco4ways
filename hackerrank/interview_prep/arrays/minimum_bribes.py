#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    # print(q)
    swaps = 0
    num_swaps = {}
    for i in range(len(q)):
        is_sorted = True
        for j in range(len(q)-i-1):
            if q[j]>q[j+1]:
                q[j], q[j+1] = q[j+1], q[j]
                swaps+=1
                is_sorted = False
                if q[j+1] in num_swaps:
                    num_swaps[q[j+1]] +=1
                else:
                    num_swaps[q[j+1]] = 1
                if num_swaps[q[j+1]] > 2:
                    print("Too chaotic")
                    return
        if is_sorted:
            break
    print(sum(num_swaps.values()))

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

