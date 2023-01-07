

a=[("a",1),("a",2),("a",3),("b",1),("b",2),("a",4),("c",1),]

d={}

for a,b in a:
    d.setdefault(a,[]).append(b)

print(d)