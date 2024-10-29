*a,=map(int,input("Enter the list seperated by spaces: ").split())
num = int(input("Enter the element: "))

for i in range(len(a)):
    if(a[i]==num):print(i,end=' ')