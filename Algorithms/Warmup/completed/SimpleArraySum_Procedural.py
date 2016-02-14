#!/bin/python3
import sys

# Definitions
def introduction():
    print("SimpleArraySum")
    print("Enter an array size, followed by the elements of the array, and SimpleArraySum will sum them for you.")
    print("")

def user_input():
    n = int(input("Enter array size ('n'): ").strip())
    summation_array = [int(arr_temp) for arr_temp in input("Enter array elements, space separated (limit = 'n'): ").strip().split(' ')]
    array_args = {"n": n, "summation_array": summation_array}
    return array_args

def calculate(array_args):
    n = array_args["n"]
    summation_array = array_args["summation_array"]
    sum = 0
    for val in summation_array:
        sum += val
    return sum

def output(sum):
    print(sum)

# Run
introduction()
array_args = user_input()
sum = calculate(array_args)
output(sum)
