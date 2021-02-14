#!/bin/python3

import os
import sys
from datetime import datetime

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    return datetime.strptime(s, "%I:%M:%S%p").strftime("%H:%M:%S%p")

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
