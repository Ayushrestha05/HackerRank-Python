
import math
import os
import random
import re
import sys


#
# Complete the 'stringAnagram' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY dictionary
#  2. STRING_ARRAY query
#

def stringAnagram(dictionary, query):
    # Write your code here
    yoyo = []
    for i in range(len(query)):
        count = 0
        for j in range(len(dictionary)):
            if sorted(query[i]) == sorted(dictionary[j]):
                count = count + 1
        yoyo.append(count)
    return yoyo


if __name__ == '__main__':

    dictionary_count = int(input().strip())

    dictionary = []

    for _ in range(dictionary_count):
        dictionary_item = input()
        dictionary.append(dictionary_item)

    query_count = int(input().strip())

    query = []

    for _ in range(query_count):
        query_item = input()
        query.append(query_item)

    result = stringAnagram(dictionary, query)
    print(result)

