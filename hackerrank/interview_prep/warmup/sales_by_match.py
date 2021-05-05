import os
import sys
import math
from collections import Counter

def sockMerchant(n, ar):
    counted = Counter(ar)
    pairs = 0
    for key in counted.keys():
        pairs += (counted[key]//2)
    return pairs



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()
