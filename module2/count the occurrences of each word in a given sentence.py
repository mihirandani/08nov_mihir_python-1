

a=input("enter a string")
print(a)
b=a.split()
print(b)

i=0
while i<len(b):
    count=0
    for j in b:
        if b[i]==j:
            count=count+1
    print(b[i],"present",count,"times")


    i=i+1