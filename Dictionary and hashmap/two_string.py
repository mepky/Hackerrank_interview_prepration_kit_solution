
import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    d={}
    l=[]
    for i in list(s1):
        if d.get(i) is not None:
            if d[i]>0:
                d[i]+=1
        else:
            d[i]=1
    for j in list(s2):
        if d.get(j) is None:
            l.append(j)
        else:
            return 'YES'
    return 'NO'

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()