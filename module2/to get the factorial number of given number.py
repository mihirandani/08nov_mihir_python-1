



a=int(input("enter your number"))
factorial=1

if a<0 :
    print("not enter negative number")

elif a==0 :
    print("fectorial o is 1")


else :
    for b in range(1,1+a) :
        factorial= factorial*b
    print(f"fectorial number{a} fectorial {factorial}")





a=7
factorial=1

if a > 0:
    for i in range(1,1+a):
       factorial=factorial*i
       print(f" number {a} factorial {factorial}")
       
print(f"{a},{factorial}")



    