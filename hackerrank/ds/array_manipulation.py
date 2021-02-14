    #!/bin/python3

    import math
    import os
    import random
    import re
    import sys

    # Complete the arrayManipulation function below.
    def arrayManipulation(n, queries):
        arr = n * [0]
        for query in queries:
            start = query[0] - 1
            end = query[1] 
            num = query[2]
            for i in range(start, end):
                arr[i]+=num
        # print(arr)
        return max(arr)

    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        queries = []

        for _ in range(m):
            queries.append(list(map(int, input().rstrip().split())))

        result = arrayManipulation(n, queries)

        fptr.write(str(result) + '\n')

        fptr.close()
