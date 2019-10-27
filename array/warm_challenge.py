import math
import os
import random
from collections import Counter
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    l=Counter(ar)
    count=0
    for i in l:
    
        count+=l[i]//2
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')