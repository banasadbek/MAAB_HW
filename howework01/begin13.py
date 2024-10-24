from math import pi
r1,r2=map(float,input("Ikkita aylana radiuslarini bo'sh joy bilan ajratib kiriting (5 6): ").split())
s1 = pi * r1
s2 = pi * r2
s3 = pi * (r1-r2)
print("S1 = %.2f"%(s1))
print("S2 = %.2f"%(s2))
print("S3 = %.2f"%(s3))