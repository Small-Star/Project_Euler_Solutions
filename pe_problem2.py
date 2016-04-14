#Project Euler - Problem 2 Solution
#01/18/2015
#
#Problem: Find sum of the even valued terms of the Fibonacci sequence that has terms less than 4000000

sum_ = 2
fib1 = 1
fib2 = 2

while True:
    #calculate next fibonacci term
    fib3 = fib1 + fib2
    print 'Fib3 ' + str(fib3)
    if fib3 >= 4000000:
        break

    #if fibonacci term is even, add it to the running sum
    if fib3 % 2 == 0:
        sum_ = sum_ + fib3
        print str(fib3) + ' ' + str(sum_)
        
    fib1 = fib2
    fib2 = fib3


print 'The sum of the even terms of the fibonacci sequence is: ' + str(sum_)
