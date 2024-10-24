from math import sqrt

def distance(x1,y1,x2,y2):
    a = abs(x1-x2)
    b = abs(y1-y2)
    distance = sqrt(pow(a,2) + pow(b,2))
    return distance

x1,y1 = map(float,input("Nuqtani bo'sh joy bilan ajratib kiriting (0 0): ").split())
x2,y2 = map(float,input("Nuqtani bo'sh joy bilan ajratib kiriting (10 10): ").split())
x3,y3 = map(float,input("Nuqtani bo'sh joy bilan ajratib kiriting (11 25): ").split())
a = distance(x1,y1,x2,y2)
b = distance(x1,y1,x3,y3)
c = distance(x3,y3,x2,y2)
P = a+b+c
p = P/2
S = sqrt(p*(p-a)*(p-b)*(p-c))
print("Yuzi: %.2f"%(S))
print("Perimetri: %.2f"%(P))