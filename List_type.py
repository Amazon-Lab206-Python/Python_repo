x = [2,3,1,7,4,12]
i = 0
y = 0
z = 0
string = ""
sum = 0

for val in x:
    if type(val) is str:
        string += val + " "
        y += 1
    elif type(val) is int or float:
        sum += val
        z +=1
    else:
        "I need a str or int"
if z and y:
    print "The list you entered is of mixed type"
    print string
    print sum
elif z:
    print "thank you for the numbers"
    print sum
else:
    print "thank you for the string"
    print string
