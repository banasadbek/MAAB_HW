a1,b1,c1,a2,b2,c2 = map(int,input("A1,B1,C1,A2,B2,C2 larni bo'sh joy bilan ajratib kiriting (1 2 3 4 5 6): ").split())

d = (a1*b2 - a2*b1)
x = (c1*b2 - c2*b1)/d
y = (a1*c2 - a2*c1)/d

print("x = %.2f"%(x))
print("y = %.2f"%(y))