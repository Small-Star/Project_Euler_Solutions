#Project Euler - Problem 3 Solution
#01/18/2015
#
#Problem: Find the largest prime factor of 600851475143

original_test_number = 600851475143
test_number = 600851475143
largest_prime_factor = 1

i = 1

def is_prime(i):
    for j in range(2,i,1):
        if i % j == 0:
            return False
    return True

while True:
    i = i + 1
    if is_prime(i) == False:
        continue
    if test_number % i == 0:
        #if it divides evenly, then i is a prime factor of the number
        if i > largest_prime_factor:
            largest_prime_factor = i
            print 'Factor: ' + str(i)

        test_number = test_number / i
        print 'New test number: ' + str(test_number)
        i = 1
    if test_number <= 2:
        #reached the end of the numbers to try
        break

print 'Largest prime factor of ' + str(original_test_number) + ' is ' + str(largest_prime_factor)

