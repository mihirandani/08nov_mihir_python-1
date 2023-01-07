"""
my_tuple=(1,2,"hello")

index=my_tuple.index(1)

print(index)

index=my_tuple.index("hello")

print(index)
"""
length=int(input("enter size of tuple:"))
my_tuple=tuple()
for i in range(length):
    temp=input("enter  tuple items:")
    my_tuple+=(temp)


elemet=input("enter an element to check:")

try:
    index = my_tuple.index(elemet)


except ValueError:
    print("element don't exist in tuple:")

else:
    print("element found in tuple:",index)