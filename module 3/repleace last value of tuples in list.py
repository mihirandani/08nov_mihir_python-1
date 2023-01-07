
tuple_list=[(23,45,20,90),(12,22,83),(1,2,3,4,5)]
for index, tuple_item in enumerate(tuple_list):
    if isinstance(tuple_item,tuple):
        new_tuple=tuple_item[:-1]+ (99,)
        tuple_list[index]= new_tuple
print(tuple_list)



tuple_list=[(23,45,20,90),(12,22,83),(1,2,3,4,5,"hello")]
for index, tuple_item in enumerate(tuple_list):
    if isinstance(tuple_item,tuple):
        new_tuple=tuple_item[:-1]+ (99,)
        tuple_list[index]= new_tuple
print(tuple_list)