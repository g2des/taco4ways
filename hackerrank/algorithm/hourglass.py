#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    max = None
    for i in range(len(arr)):
        if i + 2 >= len(arr):
            break
        for j in range(len(arr)):
            if j+2 >= len(arr):
                break
            sum = arr[i][j]
            sum += arr[i][j+1]
            sum += arr[i][j+2]
            sum += arr[i+1][j+1]
            sum += arr[i+2][j]
            sum += arr[i+2][j+1]
            sum += arr[i+2][j+2]
            if max is None or max < sum:
                max = sum
    return max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    result = hourglassSum(arr)
    # print(result)
    fptr.write(str(result) + '\n')

    fptr.close()
