# words = "It's thanksgiving day. It's my birth day too!"
# day = 'day'
# print words.find(day, 0)
# print words.replace('day','month')

# print 'Max:', max(2,54,-2,7,12,98)
# print 'Min:', min(2,54,-2,7,12,98)

# x = ["hello",2,54,-2,7,12,98,"world"]
# i = 0
# list1 = []
# print len(x)
# while i < len(x):
#     if i == 0 or i == len(x)-1:
#         print x[i]
#         list1.append(x[i])
#         i += 1
#     else: 
#         i += 1
# print list1
    
x1 = [19,2,54,-2,7,12,98,32,10,-3,6]
list2 = []
print "x1", x1
x1.sort()
print 'x1 sorted', x1
z = 0
while z < len(x1):
    if z < len(x1)/2:
        list2.append(x1[z])
        z += 1
    else:
        z += 1
x1 = x1[len(x1)/2:]
x1.insert(0, list2)
print 'x1 sorted and looped', x1
print 'l2', list2

