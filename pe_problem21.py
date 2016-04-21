#Project Euler - Problem 21 Solution
#04/20/2016

#Problem: Find the sum of all amicable numbers under 10000
#Solution: Calculate divisors for x < n; compare d values
#Usage: sum_amicables(10000,get_all_divisors(100000))

import math

def get_divisors(n):
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

def get_all_divisors(n):
    #Returns a dict with elements x:d(x) for x < n

    div_dict = {}
    for x in range(n):
        div_dict[x] = sum(get_divisors(x))

    return div_dict

def sum_amicables(n, div_dict):
    #Returns the sum of all amicable numbers < n
    #Note: the div_dict passed in needs to be considerably larger than n to account for the case where d(x) > n, even when x < n. Kludge, but for n = 10000, a div_dict of 100000 is sufficient

    sum_ = 0
    
    for i in range(n):
        if (i == div_dict[div_dict[i]]) and (i != div_dict[i]):
            #print(i)
            sum_ += i

    print('The sum of all amicable numbers less than %s is %s' %(n,sum_))

