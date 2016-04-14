#Project Euler - Problem 16 Solution
#02/01/2015
#
#Problem: Find the sum of all of the digits of 2^1000

def sum_of_digits(n_max):
    '''Returns the sum of the digits of the value 2**n_max'''
    
    n = 2**n_max

    digit_sum = 0

    for i in range(0,len(str(n)),1):
        digit_sum += int(str(n)[i])

    return digit_sum

print 'The sum of the digits of the value of 2**1000 is: ' + str(sum_of_digits(1000))
