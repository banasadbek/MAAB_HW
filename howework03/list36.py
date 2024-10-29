*a,=map(int,input("Enter the list seperated by spaces: ").split())

sm = sum(x for x in a if(x>0))

print(sm)