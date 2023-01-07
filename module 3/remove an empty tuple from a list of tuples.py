list=[(1,2,3,4),(8,9,7,6),()]
for tuple in list:
    if (len(tuple)==0):
        list.remove(tuple)
print(list)
print(tuple)