#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    return sum([1 for pair in combinations(ar, 2) if sum(pair) %k ==0])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
