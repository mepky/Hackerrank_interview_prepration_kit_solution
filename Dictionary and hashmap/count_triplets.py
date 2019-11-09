from collections import defaultdict
import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(a, r):
    m1,m2=defaultdict(int),defaultdict(int)
    count=0
    for i in reversed(a):
        if i*r in m1:
            count+=m1[i*r]
            print(count,m1)
        if i*r in m2:
            m1[i]+=m2[i*r]
            print(m2,m1)
        m2[i]+=1
    return count

    






if __name__ == '__main__':


    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    print(ans)