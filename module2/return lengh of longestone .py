


a=input("enter your line")

b=a.split()

print(a)
print(b)


largest=len(a[0])
for i in b:
    if len(i)>largest:
        largest=len(i)

print("largest string length = ",largest)