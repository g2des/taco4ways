
import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    from collections import Counter
    from functools import reduce
    counter = Counter(arr)
    total_gps = 0
    for key in counter:
        triplet = (key, key*(r**1),key*(r**2))
        vals = [counter[num] for num in triplet]
        total_gps += reduce(lambda x, y: x*y,vals)
    return total_gps
        
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()

