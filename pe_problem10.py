#Project Euler - Problem 1 Solution
#01/18/2015
#
#Problem: Find the sum of all primes below 2000000

from math import sqrt
max_prime = 2000000

def is_prime(i):
    if i < 47:
        for j in range(2,i,1):
            if i % j == 0:
                return False
    else:
        for j in [2,3,5,7,11,13,17,19,23,29,31,37,41,43]:
            if i % j == 0:
                return False
        for j in range(47,int(sqrt(i)) + 1,1):
            if i % j == 0:
                return False
    return True

sum_ = 0

for p in range(2,max_prime,1):
    if is_prime(p):
        sum_ = sum_ + p

print 'The sum of all primes up to ' + str(max_prime) + ' is ' + str(sum_)
