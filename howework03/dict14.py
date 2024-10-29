a = {'a': 1, 'b': 2, 'c': 3}
value = int(input("Enter the value: "))

b = [key for key in list(a.keys()) if(a.get(key)==value)]

print(b)