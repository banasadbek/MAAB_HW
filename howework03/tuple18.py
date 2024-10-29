a = (1,2,3,4,5,6,7,8,9,1,2,3,54,2,1,3,5,6,3,21,34,6,3,2)

n,m = map(int,input("Enter the beginning and ending indexs of the subtuple seperated by a space: ").split())

print(min(a[n:m+1]))