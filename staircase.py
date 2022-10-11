"""import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#"""

def staircase(n):
    for i in range(1,n+1):
        s = "#" * i
        print(s.rjust(n)) #The rjust() method will right align the string, using a specified character (space is default) as the fill character.
        
"""if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)"""
