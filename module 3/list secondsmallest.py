

a=[]
size = int(input("enter your size list:"))

for i in range(size):
    val=int(input("enter number:"))
    a.append(val)
minimum=min(a)
print(minimum)

a.sort()
print("min number=",a[0])
print("second min value=",a[1])