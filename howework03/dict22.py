a = {'a': 3, 'c': 2, 'b': 1}

b = {key: value for key, value in a.items() if(value<3)}

print(b)