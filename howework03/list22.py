*a,=map(int,input("Enter the list seperated by spaces: ").split())

b = [x for x in a if x%2==0]

print(b)