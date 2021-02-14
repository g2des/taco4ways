#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    zeros = 0
    pos = 0
    neg = 0
    for num in arr:
        if num is 0:
            zeros +=1
        elif num > 0:
            pos +=1
        else:
            neg +=1
    print("{:.6f}".format(pos/(pos+neg+zeros)))
    print("{:.6f}".format(neg/(pos+neg+zeros)))
    print("{:.6f}".format(zeros/(pos+neg+zeros)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)