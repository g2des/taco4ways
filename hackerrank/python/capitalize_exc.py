#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    shift = True
    another = list()
    char = None
    for i in range(len(s)):
        char = s[i]
        if s[i] is " " or i == 0:
            shift = True
        if s[i] is not " ":
            if shift is True:
                # print("Here")
                char = s[i].upper()
            shift = False
        another.append(char)
    # print("".join(another))
    return "".join(another)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()
