from math import sqrt
a,b,c = map(int,input("[Ax^2 + Bx + C = 0] A,B,C ni bo'sh joy bilan ajratib kiriting (1 5 3): ").split())
d = pow(b,2) - 4*a*c

if(d>=0):
    x1 = -b + sqrt(d)
    x2 = -b - sqrt(d)
    print("x1 = %.2f"%(x1))
    print("x2 = %.2f"%(x2))
else:
    print("Yechimga ega emas")