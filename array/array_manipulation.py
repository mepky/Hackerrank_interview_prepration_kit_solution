#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, q):
    l=[0]*(n+1)
    for i in q:
        l[i[0]-1]+=i[2]
        if i[1]!=n:
            l[i[1]]-=i[2]
    p=0
    maxval=0

    for j in l:
        p+=j
        if p>maxval:
            maxval=p
    return maxval
   



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
