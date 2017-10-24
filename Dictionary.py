myinfo = {
    'first name': 'Noah',
    'last name': 'Hendry',
    'favorite language': 'python',
    'birth state': 'AZ',
    'age': '20'
}
def info():
    for key, val in myinfo.items():
        print 'my ' + key + ' is ' + val

info()