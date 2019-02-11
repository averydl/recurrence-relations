'''
Code written by Derek Avery
2019/02/11

Module includes a function to recursively
print all possible arrangements of 2x1 dominos
in a grid with dimensions 2xN
'''

import sys

# Prints all possible combinations of stacking
# 2x1 dominos in a grid of dimensions 2xN, where N
# is the length of the grid of width 2. The 'N
# parameter may be specified as a command line argument
def tile(length, previous):
    if length == 1: # initial condition: T(1) = 1
        print(previous + "|")
    elif length == 2: # initial condition: T(2) = 2
        print(previous + "=")
        print(previous + "||")
    else: # general case: recursively call tile function on strings with '|' and '=' appended
        tile(length-1, str(previous) + "|")
        tile(length-2, str(previous) + "=")

tile(int(sys.argv[1]), "")
