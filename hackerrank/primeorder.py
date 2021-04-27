#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'sortOrders' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY orderList as parameter.
#


def sortOrders(orderList):
    # Write your code here
    primeOrders = []
    nonPrimeOrders = []
    for index, order in enumerate(orderList):
        sortStringList = order.split(" ")
        print(sortStringList)
        sortString = "".join(sortStringList[1:]) + sortStringList[0]
        identifierString = "".join(sortStringList[1:])
        if identifierString.isnumeric():
            print(identifierString)
            nonPrimeOrders.append((index, sortString))
        else:
            print("prime", identifierString)
            primeOrders.append((index, sortString))
    sorted(primeOrders, key=lambda item:item[1])
    sorted(nonPrimeOrders, key=lambda item:item[1])
    return [orderList[index] for index, _ in reversed(primeOrders)]+[orderList[index] for index, _ in nonPrimeOrders ]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    orderList_count = int(input().strip())

    orderList = []

    for _ in range(orderList_count):
        orderList_item = input()
        orderList.append(orderList_item)

    result = sortOrders(orderList)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
