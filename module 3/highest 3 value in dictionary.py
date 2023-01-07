

fruets={ "banana":10,"apple":30,"panapple":20,"whtermeran":8}

costly_fruets=sorted(fruets,key=fruets.get,reverse=False)


for index in range(3):
    print(costly_fruets[index])


print()

costly_fruets=sorted(fruets,key=fruets.get,reverse=True)


for index in range(3):
    print(costly_fruets[index])