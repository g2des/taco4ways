#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getCost' function below.
#
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#

def getCost(g_nodes, g_from, g_to, g_weight):
    print(g_nodes, g_from, g_to, g_weight)
    def calculate(end, fare):
        if end is 1:
            return fare
        minimum = None
        indices = [i for i,x in enumerate(g_to) if x == end]
        for  index in indices:
            start = g_from[index]
            cost = g_weight[index]
            
    calculate(g_nodes, 0)       
    return 0

if __name__ == '__main__':
    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    getCost(g_nodes, g_from, g_to, g_weight)
