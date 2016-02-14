#!/bin/python3
import sys

# User Introduction
# print("SimpleArraySum")
# print("Enter an array size, followed by the elements of the array, and SimpleArraySum will sum them for you.")
# print("")

# Input
n = int(input().strip())
summation_array = [int(arr_temp) for arr_temp in input().strip().split(' ')]

# Calculation
sum = 0
for val in summation_array:
    sum += val

# Output
print(sum)
