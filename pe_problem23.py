#Project Euler - Problem 23 Solution
#04/27/2016

#Problem: Find the sum of all the positive numbers which cannot be written as the sum of two abundant integers
#Solution: Find abundant integers; check all n < 28123 to see if n can be written as the sum of 2 abundant integers; sum

import math

def get_proper_divisors(n):
    divisors = []
    divisors_ret = []
    i = 0
    s = int(math.sqrt(n))
    
    while True:
        i += 1
        if n % i == 0:
            divisors.append(i)
        if i > s:
            break

    #Because we are only finding the divisors up to the sqrt, add in the remaining ones
    for k in divisors:
        if k not in divisors_ret:
            divisors_ret.append(k)
        if int(n/k) not in divisors_ret and k != 1:
            #According to the problem, n is not a divisor of n, yet 1 is. Cut out n
            divisors_ret.append(int(n/k))

    return divisors_ret

def is_abundant(n):
    #Returns true if abundant

    if sum(get_proper_divisors(n)) > n:
        return True
    else:
        return False
    
def list_of_abundant_nums(n):
    #Returns a list of all abundant numbers < n

    abundants = []

    for i in range(4,min(n,28124)): #Cut out 0 and 2, which do not count as abundant
        if is_abundant(i):
            abundants.append(i)

    return abundants

def cannot_be_sum_of_abundants(n, abundants):
    #Returns True if n cannot be written as the sum of abundants

    if n > 28123:
        return False
    else:
        for a in abundants:
            if a > n:
                continue
            #Check all abundants, if the number - test value is also in the abundants list, than the numbner can be the sum of 2 abundants
            elif (n - a) in abundants:
                return False
        return True

def sum_non_abundant_sums(n): #Ugh, what clunky names
    #Returns the sum of all numbers up to n which cannot be written as the sum of abundants

    abundants = list_of_abundant_nums(n)

    print(sum([i*cannot_be_sum_of_abundants(i,abundants) for i in range(n)]))
