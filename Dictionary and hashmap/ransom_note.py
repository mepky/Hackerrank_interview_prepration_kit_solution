
import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    hash_word={}
    for word in magazine:
        if hash_word.get(word)!=None:
            if hash_word[word]>0:
                hash_word[word]+=1
        else:
            hash_word[word]=1

    for r_word in note:
        if hash_word.get(r_word) is None or hash_word[r_word]==0:
            return 'No'
        else:
            hash_word[r_word]-=1
    return 'Yes'



if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))