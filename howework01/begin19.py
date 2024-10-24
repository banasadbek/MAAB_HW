x1,y1 = map(float,input("Nuqtani bo'sh joy bilan ajratib kiriting (0 0): ").split())
x2,y2 = map(float,input("Nuqtani bo'sh joy bilan ajratib kiriting (10 10): ").split())
a = abs(x1-x2)
b = abs(y1-y2)
P = 2*(a+b)
S = a*b
print("Yuzi:",S,"\nPerimetri:",P)