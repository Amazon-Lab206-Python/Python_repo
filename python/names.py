
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
for key in users:
    print key.upper()
    for i in range(len(users[key])):
        print i+1, users[key][i]["first_name"].upper(), users[key][i]["last_name"].upper(), len(users[key][i]["first_name"]+ users[key][i]["last_name"])

# def show_all(users):
#     for job in users:
#         counter = 0
#         print job
#         for person in users[job]:
#             counter += 1
#             first_name = person['first_name'].upper()
#             last_name = person['last_name'].upper()
#             length = len(first_name) + len(last_name)
#             print "{} - {} {} - {}".format(counter, first_name, last_name, length)

# show_all(users)
