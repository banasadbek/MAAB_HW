*a,=map(int,input("Enter the list seperated by spaces: ").split())
n = int(input("Enter the element that needs to be replaced"))
m = int(input("Enter the number that you want to put"))

a[a.index(n)] = m
print(a)