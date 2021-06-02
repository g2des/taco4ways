#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    # Write your code here
    
    magazine_dict = {}
    all_words_present = True
    for word in magazine:
        if word in magazine_dict:
            magazine_dict[word] += 1
        else:
            magazine_dict[word] = 1
    for word in note:
        if word in magazine_dict:
            magazine_dict[word] -= 1
            if magazine_dict[word] == 0:
                magazine_dict.pop(word)
        else:
            all_words_present = False
    if all_words_present:
        print("Yes")
    else:
        print("No")
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)


