#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.

def minimumSwaps(arr): 
    swaps = 0
    getIndex = dict(zip(arr,range(1,len(arr)+1)))
    for i in range(1,len(arr)+1):
        #swap only if value is not equal to index
        if getIndex[i]!=i: 
            getIndex[arr[i-1]]=getIndex[i]
            arr[getIndex[i]-1]=arr[i-1]
            swaps+=1
    return swaps 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

