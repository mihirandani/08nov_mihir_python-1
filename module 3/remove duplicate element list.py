

a=int(input("enter the total number of element you want inside your list"))    

b=[]                                  #list ma lakhava mate


for m in range(a):                                  #loop feravava mate a hoy etali var lop fare
    city = input("enter city name")

    b.append(city)
print("city name",b)

c=set(b)                                    # change for list to set
print("non duplicate value",c)