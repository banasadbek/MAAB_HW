*a,=map(int,input("Enter the list seperated by spaces: ").split())
n,m = map(int,input("Enter the value and the index seperated by a space: ").split())

a.insert(m,n)
print(a)