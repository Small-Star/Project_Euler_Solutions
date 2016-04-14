#Project Euler - Problem 7 Solution
#01/18/2015
#
#Problem: Find the 10001st prime

def is_prime(i):
    for j in range(2,i,1):
        if i % j == 0:
            return False
    return True

prime_to_find = 10001
prime_ctr = 0
p = 2

while prime_ctr < prime_to_find:
    if is_prime(p) == True:
        prime_ctr = prime_ctr + 1
    p = p + 1
        
print 'The ' + str(prime_ctr) + 'th prime is: ' + str(p - 1)
