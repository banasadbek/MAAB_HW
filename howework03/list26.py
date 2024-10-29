*a,=map(int,input("Enter the list seperated by spaces: ").split())

n = len(a)
if(n%2):print(a[(n+1)//2-1])
else:print(a[(n+1)//2-1],a[(n+1)//2])