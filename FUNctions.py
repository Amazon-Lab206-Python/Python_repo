def odd_even():
    for val in range(0,2001):
        if val % 2 == 1:
            print 'number is ' + str(val) + '. This is an odd number'
        else:
            print 'number is ' + str(val) + '. This is an even number'  

odd_even()

def multiply(arr):
    for val in arr:
        print val * 5   
    
multiply([2,4,10,16])