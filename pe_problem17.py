#Project Euler - Problem 17 Solution
#02/01/2015
#
#Problem: Find the number of letters require to write all of the numbers between one and 1000

def number_of_letters():

    digit_sum = 0
    
    num_dict = {1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4,10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8}
    tens_num_dict = {2:6,3:6,4:5,5:5,6:5,7:7,8:6,9:6}

    digits = {}

    #1 - 19    
    for i in range(1,20,1):
        digits[i] = num_dict.get(i,0)

    #20 - 99
    for i in range(20,100,1):
        digits[i] = (tens_num_dict[i/10] + num_dict.get(i%10,0))

    #Set the 2 LSDs for the rest of the numbers
    for i in range(100,1001,1):
        if digits.get(i,0) == 0:
            if not digits.get(i/100,0) == 0:
                digits[i] = digits.get(i%100,0)

    for i in range(100,1000,1):
        #Add 'hundred'
        digits[i] += 7

        #For the non-hundred (i.e. 100, 200, etc) add 'and'
        if i % 100 != 0:
            digits[i] += 3

        #Add in the value for the hundreds signifier
        digits[i] += num_dict[i/100]

    #Take care of 1000
    digits[1000] = 11
    
    print digits

    print 'The number of letters required to write out the first 1000 numbers is: ' + str(sum(digits.values()))



