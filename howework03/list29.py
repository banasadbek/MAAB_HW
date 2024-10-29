*a,=map(int,input("Enter the list seperated by spaces: ").split())
inx = int(input("Enter the index: "))

if(len(a)>inx): a.pop(inx)

print(a)