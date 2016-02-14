#!/bin/python3
# - Imports
import sys

# - Input
# print("Enter 'n', denoting matrix width and height.")
n = int(input().strip())

# - Sum Matrix Diagonals
dSumLeft = 0
dSumRight = 0
## Do a running sum for each diagonal, row by row, as entered.
for i in range(n):
    ## Row input.
    matrixRow = input().split()
    ## Adds i'th row value to the left diagonal sum.
    dSumLeft += int(matrixRow[i])
    ## Adds -i'th row value to the left diagonal sum.
    dSumRight += int(matrixRow[-(i + 1)])

    ## - Row Status Updates
    # print("Row {}: ".format(i+1), matrixRow)
    # print("L->R Diagonal Running Sum: ", dSumLeft)
    # print("R->L Diagonal Running Sum: ", dSumRight)

# - Absolute Difference
abs_diff = abs(dSumLeft - dSumRight)

# - Output
print(abs_diff)
