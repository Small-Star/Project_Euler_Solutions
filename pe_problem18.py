#Project Euler - Problem 18 Solution
#02/05/2015
#
#Problem: Find the highest sum creating by following a path downward in a triangle of numbers

#Process: Don't bruteforce it, but iteratively compute from the bottom up

#Data Munging
triangle = {}
triangle[0] = {}
nums = [75, 95, 64, 17, 47, 82, 18, 35, 87, 10, 20, 04, 82, 47, 65, 19, 01, 23, 75, 03, 34, 88, 02, 77, 73, 07, 63, 67, 99, 65, 04, 28, 06, 16, 70, 92, 41, 41, 26, 56, 83, 40, 80, 70, 33, 41, 48, 72, 33, 47, 32, 37, 16, 94, 29, 53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14, 70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57, 91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48, 63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31, 04, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 04, 23]

j = 0
k = 0

for i in nums:
    triangle[j][k] = i
    if k == j:
        k = 0
        j +=1
        triangle[j] = {}
        continue
    k += 1

#Remove last row
del triangle[j]

#for each element (other than the bottom row), add the greater of the two elements immediately below. Answer will be the top of the pyramid
for j in range(len(triangle) - 2,-1,-1):
    for k in range(0,len(triangle[j]),1):
    #start from one row from the bottom, let the value become += max(the two values below)
        triangle[j][k] += max(triangle[j + 1][k], triangle[j + 1][k + 1])

print 'The largest sum is: ' + str(triangle[0][0])
