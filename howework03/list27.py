*a,=map(int,input("Enter the list seperated by spaces: ").split())
n,m = map(int,input("Enter the beginning and ending indexs of the sublist seperated by a space: ").split())

print(max(a[n:m+1]))