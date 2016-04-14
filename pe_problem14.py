#Project Euler - Problem 14 Solution
#01/25/2015
#
#Problem: Which Collatz sequence starting under 1000000 has the longest number of terms

#Process:   For a given number, calculate the sequence
#           If a term in the sequence has a sequence, sequence is over
#           Store number of terms in sequence

test_max = 1000000
num_terms = 0
largest_num_terms = 0
largest_seq = 0

num_terms_in_chain = {}

def generate_collatz_sequence(num):
    seq = [num]
    terms = 1

    j = num
    
    while j != 1:
        if j in num_terms_in_chain:
            #this part of the sequence has already been computed
            terms += num_terms_in_chain[j] - 1
            break
        else:
               #this sequence has not been computed
            if j % 2 == 0:
                #term is even
                j = j / 2
            else:
                j = (3 * j) + 1
        terms += 1
    
    return terms

for i in range(1,test_max,1):
    #Loop through all terms
    num_terms = generate_collatz_sequence(i)
    num_terms_in_chain[i] = num_terms 
    if num_terms > largest_num_terms:
        largest_num_terms = num_terms
        largest_seq = i

print 'The largest sequence is ' + str(largest_num_terms) + ' terms long, and begins with number ' + str(largest_seq)
