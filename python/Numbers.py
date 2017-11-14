# for range in range (1, 1001): # starting at 1 and running to 1000
#     print range # printing as it goes
#     range += 1 # 1>2>3..........1000,

# for fifths in range (5,1000001 , 5): #Same as above in increments of 5
#     print fifths
#     fifths += 5

i = 0
sum = 0
a = [1, 2, 5, 10, 255, 3] 
while i < len(a): #
    sum += a[i]
    i +=1
print sum
sum = sum/len(a)
print sum