a = {'a': 3, 'c': 2, 'b': 1}

b = dict(sorted(a.items(), key=lambda item: item[1]))

print(b)