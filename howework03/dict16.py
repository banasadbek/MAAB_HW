a = {'a': 1, 'b': 2, 'c': {'d': 4}}
t=0
for value in a.values():
    if isinstance(value, dict):
        t=1
print("Yes"if(t)else"No")