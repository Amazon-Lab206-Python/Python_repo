def dictToTup(my_dict):
    newtup = []
    for keys, val in my_dict.items():
        newtup.append((keys,val))
    print newtup
    return newtup

my_dict = {
    "Speros": "(555) 555-5555",
    "Michael": "(999) 999-9999",
    "Jay": "(777) 777-7777"
}
dictToTup(my_dict)

