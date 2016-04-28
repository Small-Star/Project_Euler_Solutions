#Project Euler - Problem 22 Solution
#04/20/2016

#Problem: Find the name score (see problem)
#Solution: Straighforward

import os
import functools

def name_score(fname):

    if not os.path.isfile(fname):
        print('%s does not exist' %fname)
        return 0

    f = open(fname, "r")

    names = str(f.read()[1:]).split(',"') #Skip leading quote
    names = [n[:-1] for n in names]

    cnt = 1
    scores = []
    
    for n in sorted(names):
        tot = sum([ord(c) - 64 for c in n])*cnt
        scores.append(tot)
        #print(n,sum([ord(c) - 64 for c in n]),cnt,tot)
        cnt += 1
        
    print('The sum of name scores is: %s' %sum(scores))
                       

