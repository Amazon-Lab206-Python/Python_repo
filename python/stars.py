def drawStars(arr):
     for val in arr:
        if type(val) == int:
            print '*'*val
        else:
            print val[0].lower() * len(val)

drawStars([4, 4, 1, 4, 5, 7, 4])