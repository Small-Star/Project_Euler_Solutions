#Project Euler - Problem 5 Solution
#01/18/2015
#
#Problem: Find the smallest positive number evenly divisible by the numbers 1 - 20

test_num = 20
divisible_flag = 0

while True:

    for i in [20,19,18,17,16,15,14,13,12,11]:
        if test_num % i != 0:
            divisible_flag = 0
            break
        else:
            divisible_flag = 1
            #print str(test_num) + ' is divisible by : ' + str(i)

    if divisible_flag == 1:
        #if the number is divisible by 1 - 20, it is the smallest number so divisible, as testing was started from the bottom up
        break

    #reset loop
    divisible_flag = 0
    #print test_num
    test_num = test_num + 20
    
print 'Smallest number evenly divisible by all numbers 1 - 20 is: ' + str(test_num)
