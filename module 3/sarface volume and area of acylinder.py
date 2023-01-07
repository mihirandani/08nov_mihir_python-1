
import math

def surfacevolume (h,r):
    return(math.pi *r * r * h)



def area (h,r):
    return((2 * math.pi * r * h) + (2 * math.pi * math.pow(r,2)))



h = float(input("enter height of the cylinder:"))

r = float(input("enter radius of the cylinder:"))

vol = surfacevolume(h,r)
ar = area(h,r)

print("surface:{0,.2f}",format(vol))
print("area:{0,.2f}",format(ar))
