*a,=map(int,input("Enter the list1 seperated by spaces: ").split())
*b,=map(int,input("Enter the list2 seperated by spaces: ").split())

c = a.copy()
c.extend(b)

print(c)