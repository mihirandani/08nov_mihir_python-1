

a= "mihir"
b= "andani"


a=input("enter a")

b=input("enter b")

x=a[0:2]

a=a.replace(a[0:2],b[0:2])

b=b.replace(b[0:2],x)

print(a,b)