#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    min =scores[0]
    max = scores[0]
    count_max = 0
    count_min = 0
    for score in scores:
        if score > max :
            count_max +=1
            max = score
        elif score < min:
            count_min +=1
            min = score
    return (count_max, count_min)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
