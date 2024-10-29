*a,=map(int,input("Enter the list seperated by spaces: ").split())
*b,=map(int,input("Enter the sub-list seperated by spaces: ").split())


print(' '.join(map(str, b)) in ' '.join(map(str, a)))