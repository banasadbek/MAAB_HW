a = {'a': 3, 'c': 2, 'b': 1}

b = {key: a[key] for key in sorted(a)}

print(b)