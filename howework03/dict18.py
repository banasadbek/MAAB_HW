from collections import defaultdict

a = defaultdict(lambda: 'Not Found')

a['a'] = 1
a['b'] = 1

print(a['a'])
print(a['c'])

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

print(x)