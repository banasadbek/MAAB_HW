a,b = map(int,input("Ikkita sonni bo'sh joy bilan ajratib kiriting (13 24): ").split())
# version1 a,b=b,a
# version2 using algebra

#version2
a += b
b = a-b
a = a-b
print(a,b)