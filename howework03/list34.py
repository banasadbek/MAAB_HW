*a,=map(int,input("Enter the list seperated by spaces: ").split())
num = int(input("Enter shifting number: "))

num %= len(a)

b = a[-num:] + a[:-num]

print(b)