#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(n):
        hash = i+1
        space = n - hash
        print("".join([" "*space])+"".join(["#"*hash]))

if __name__ == '__main__':
    n = int(input())

    staircase(n)
