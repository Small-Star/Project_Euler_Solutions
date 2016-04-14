#Project Euler - Problem 9 Solution
#01/18/2015
#
#Problem: Find product of the Pythagorean triplet in which the 3 values sum to 1000

#Process: Try all combinations of a and b < 500

def is_pythagorean_triplet(a,b,c):
    '''Finds out if the 3 given values are a Pythagorean Triplet'''
    if a > b:
        return False
    if b > c:
        return False
    if a**2 + b**2 != c**2:
        return False
    else:
        return True

for a in range(1,501,1):
    for b in range(1,501,1):
        if is_pythagorean_triplet(a,b,1000 - a - b) == True:
            print 'The Pythagorean Triplet with values summing to 1000 is: ' + str(a) + ', ' + str(b) + ', '+ str(1000 - a - b)
            print 'The product of the triplet is: ' + str(a*b*(1000 - a - b))
        
