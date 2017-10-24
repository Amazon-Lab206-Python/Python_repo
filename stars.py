def drawStars(arr):
    for val in arr:
        if type(val) is int:
            print '*' * val
        else:
            print val[0].lower() * len(val)

drawStars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])