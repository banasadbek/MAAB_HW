a = (1,2,3,4,5,6,7,8,9,1,2,3,54,2,1,3,5,6,3,21,34,6,3,2)
num = int(input("Enter a number: "))

b = list(a)
b.pop(b.index(num))
b = tuple(b)

print(b)