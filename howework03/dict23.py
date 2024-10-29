a = {'a': 1, 'b': 2, 'c': 3}
b = {'d': 4, 'e': 5, 'f': 6}

c = set(a.keys()) & set(b.keys())
print(bool(c))