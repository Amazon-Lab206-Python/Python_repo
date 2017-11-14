import random

def coinFlip(rounds):
    heads = 0
    tails = 0
    output = ''
    for i in range(1,rounds+1):
        if random.randint(0,1):
            heads += 1
            output = 'heads'
        else:
            tails += 1
            out = 'tails'
        print "Flip #{} Throwing... It's {}! {} for heads and {} for tails so far!".format(i,output,heads,tails)
coinFlip(100000)
