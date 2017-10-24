import random

def coinFlip(rounds):
    heads = 0
    tails = 0
    for i in range(1,rounds):
        if round(random.randint(0,1)) == 1:
            heads += 1
            print "Flip #"+ str(i) + " Throwing... It's heads! " + str(heads) + " for heads and " + str(tails) + " for tails so far!"
        else:
            tails += 1
            print "Flip #"+ str(i) + " Throwing... It's tails! " + str(heads) + " for heads and " + str(tails) + " for tails so far!"
coinFlip(5000)
