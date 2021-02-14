#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def lcm(x, y):
    return int(round(x*y / math.gcd(x,y)))

def getTotalX(a, b):
    lcm_a = lcm(a[0], a[1]) if len(a)>1 else a[0]
    if len(a) > 2:
        for i in range(2, len(a)):
            lcm_a = lcm(lcm_a, a[i])
    gcd_b = math.gcd(b[0],b[1]) if len(b)>1 else b[0]
    if len(b) > 2:
        for i in range(2, len(b)):
            gcd_b = math.gcd(b[i], gcd_b)

    out = [x for x in range(lcm_a, min(b)+1, lcm_a) if gcd_b%x == 0]
    return len(out)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)
    print(total)
    fptr.write(str(total) + '\n')

    fptr.close()
