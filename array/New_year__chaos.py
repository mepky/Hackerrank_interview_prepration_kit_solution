#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    count=0
    n=len(q)
    i=0
    l=[0]*n
    swap=True
    while swap:
        swap=False
        for i in range(n):
            while i<n-1 and q[i]>q[i+1]:
                l[q[i]-1]+=1
                q[i],q[i+1]=q[i+1],q[i]
                swap=True
                i+=1
    k=0
    for s in l:
        k+=s

        if s>2:
            return ("Too chaotic")
        
    else:
        return k




if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
