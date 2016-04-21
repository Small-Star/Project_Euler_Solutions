#Project Euler - Problem 20 Solution
#04/20/2016

#Problem: Calculate the sum of the digits of 100!
#Solution: Straightforward

import math

def sum_of_digits_of_factorial(n):
    
    s = str(math.factorial(n))
    return sum([int(x) for x in s])
