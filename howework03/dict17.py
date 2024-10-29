a = {'a': 1, 'b': 2, 'c': {'d': 4}}
t=0
for value in a.values():
    if isinstance(value, dict):
        print(list(value.values())[0])