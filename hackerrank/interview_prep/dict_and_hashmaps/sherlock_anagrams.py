#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    s_substrings = dict()
    
    for i in range(1, len(s)+1):
        for j in range(0,len(s)+1,1):
            substr = s[j:j+i]
            if len(substr) == i:
                substr_sorted = "".join(sorted(list(substr)))
                print(substr, j, j+1)
                num_elements =s_substrings.get(substr_sorted, 0)
                s_substrings[substr_sorted] =  num_elements + 1
            else:
                break
    total_len = 0
    for value in s_substrings.values():
        total_len += ((value*(value-1))//2)
    print(s_substrings)
    return total_len

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()

