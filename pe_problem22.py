#Project Euler - Problem 22 Solution
#04/20/2016

#Problem: Find the name score (see problem)
#Solution: Straighforward

import os

def name_score(fname):

    if not os.path.isfile(fname):
        print('%s does not exist' %fname)
        return 0

    f = open(fname, "r")

    names = str(f.read()).split(',"')
    names = [n[:-1] for n in names]
##    for n in names:
##        print("poop",n)

##    print(len(names))
