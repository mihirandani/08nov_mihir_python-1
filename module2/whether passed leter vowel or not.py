
x=input("enter a senrence: ")
count=0
for i in x:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        print(i)
        count=count+1


if count==0:
    print("no vowel found")

else:
    print("number of vowels:",count)