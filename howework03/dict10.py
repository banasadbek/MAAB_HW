a = {'a': 1, 'b': 2, 'c': 3}
key = input("Enter a key: ")

if(key in a.keys()):
    print(key,a.get(key))