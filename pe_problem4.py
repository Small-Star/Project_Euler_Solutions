#Project Euler - Problem 4 Solution
#01/18/2015
#
#Problem: Find the largest palindrome made from the product of 2 3 digit numbers

largest_palindrome_product = 0

char = 0

def is_palindrome(palindrome):
    for char in range(0,len(palindrome)/2,1):
        if palindrome[char] != palindrome[len(palindrome) - 1 - char]:
            return False
    return True



for i in range(100,1000,1):
    for j in range(100,1000,1):
        #Loop through all posible number combinations
        temp_result = i * j
        if is_palindrome(str(temp_result)): 
            if temp_result > largest_palindrome_product:
                largest_palindrome_product = temp_result

print 'Largest palindrome product is: ' + str(largest_palindrome_product)
