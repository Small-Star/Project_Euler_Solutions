#Project Euler - Problem 1 Solution
#01/18/2015
#
#Problem: Find sum of the multiples of 3 or 5 below 1000

num_ceiling = 1000
sum_ = 0

for i in range(1,num_ceiling,1):
    if (i % 3 == 0) or (i % 5 == 0):
        #if i%3 or i%5 has a 0 remainder, the number is a multiple of 3 or 5
        sum_ = sum_ + i

print 'Sum of the multiples of 3 or 5 below ' + str(num_ceiling) + ' is ' + str(sum_)
