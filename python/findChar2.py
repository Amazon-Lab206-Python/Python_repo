newlist = []
words = ['hello','world','my','name','is','Anna']
char = 'o'
for i in range(0, len(words)):
        if words[i].find(char) != -1:
            newlist.append(words[i])

print newlist

    
