#Project Euler - Problem 12 Solution
#01/25/2015
#
#Problem: Find the first triangle number to have over 500 divisors

import math

def get_nth_triangle_number(n):
    return sum(range(1,n+1,1))

def get_divisors(n):
    divisors = []
    divisors_clone = []
    i = 0
    while True:
        i += 1
        if n % i == 0:
            divisors.append(i)
        if i > int(math.sqrt(n)):
            break

    #because we are only finding the divisors up to the sqrt, add in the remaining ones
    for k in divisors:
        divisors_clone.append(k)
        divisors_clone.append(n/k)

    return divisors_clone

def get_num_divisors(n):
    divisors = 0
    i = 0
    while True:
        i += 1
        if n % i == 0:
            divisors += 1
        if i > int(math.sqrt(n)):
            break

    return divisors * 2

j = 1

while True:
    num_divs = get_num_divisors(get_nth_triangle_number(j))
    if  num_divs >= 500:
        print 'The first number with ' + str(num_divs) + ' divisors is: ' + str(get_nth_triangle_number(j))
        print 'This was the ' + str(j) + 'th triangle number'
        break
    if j % 10 == 0:
        print 'Trying ' + str(j) + 'th triangle number'
    j += 1
