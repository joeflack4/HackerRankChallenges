#!/bin/python3
import sys

# AVeryBigSum
# The purpose of this challenge is in dealing with long integers.
# However, Python automatically deals with int and long int, and there is no overflow.
# Therefore this sourcecode is identical to that of the challenge SimpleArraySum.

# Input
n = int(input().strip())
summation_array = [int(arr_temp) for arr_temp in input().strip().split(' ')]

# Calculation
sum = 0
for val in summation_array:
    sum += val

# Output
print(sum)
