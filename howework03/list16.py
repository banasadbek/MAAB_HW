*a,=map(int,input("Enter the list seperated by spaces: ").split())

cnt=0
for i in a:
    if(i%2):cnt+=1

print(cnt)