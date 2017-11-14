import random

def grades(students):
    for i in range(students):
        score = random.randint(60,100)
        if  59 < score < 70:
            print 'Score: ' + str(score) + '; Your grade is a D'
        elif  69 < score < 80:
            print 'Score: ' + str(score) + '; Your grade is a C'
        elif  79 < score < 90:
            print 'Score: ' + str(score) + '; Your grade is a B'
        elif  89 < score < 101:
            print 'Score: ' + str(score) + '; Your grade is a A'
        else:
            print score
            print 'Yikes'


grades(10)