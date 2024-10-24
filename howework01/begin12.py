from math import sqrt
a,b=map(float,input("To'g'ri uchburchakning tomonlarini bo'sh joy bilan ajratib kiriting (5 6): ").split())
c = sqrt(pow(a,2) + pow(b,2))
P = a+b+c
print("c =",c,"\nPerimetri:",P)