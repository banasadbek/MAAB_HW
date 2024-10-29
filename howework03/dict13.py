a = {'a': 1, 'b': 2, 'c': 3}

b = {value: key for key, value in a.items()}

print(b)