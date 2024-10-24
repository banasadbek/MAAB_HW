from math import sqrt
x1,y1 = map(float,input("Nuqtani bo'sh joy bilan ajratib kiriting (0 0): ").split())
x2,y2 = map(float,input("Nuqtani bo'sh joy bilan ajratib kiriting (10 10): ").split())
a = abs(x1-x2)
b = abs(y1-y2)
distance = sqrt(pow(a,2) + pow(b,2))
print("Orasidagi masofa: %.2f"%(distance))