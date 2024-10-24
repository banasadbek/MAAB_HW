a,b,c=map(float,input("Paralelepiped tomonlarini bo'sh joy bilan ajratib kiriting (5 6 3): ").split())
V = a * b * c
S = 2 * (a*b + b*c + a*c)
print("Hajmi: {}\nTo'la sirti: {}".format(V,S))