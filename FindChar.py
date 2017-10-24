def findchar(words, char):
    newlist = []
    for i in range (0,len(words)):
        if words[i].find(char) != -1:
            newlist.append(words[i])

    print newlist

test_list = ['hello','world','name','is','anna']
findchar(test_list,'o')