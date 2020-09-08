#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    print(arr)
    max = arr[len(arr) - 1]
    min = arr[0]
    max_sum = 0
    min_sum = 0

    for i in range(0, len(arr) - 1, 1):
        max_sum = max_sum + arr[i]

    for i in range(len(arr) - 1, 0, -1):
        min_sum = min_sum + arr[i]

    print(max_sum, min_sum)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
