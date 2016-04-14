#Project Euler - Problem 6 Solution
#01/18/2015
#
#Problem: Find the difference between the sum of the squares of the integers 1 - 100 and the square of the sum of the integers 1 - 100

sum_ = 0
sum_of_squares = 0

max_range = 100

for i in range(1,max_range + 1,1):
    sum_ = sum_ + i
    sum_of_squares = sum_of_squares + i**2

square_of_sum = sum_**2

print 'The difference between the sum of the squares and the square of the sums is: ' + str(square_of_sum - sum_of_squares)
