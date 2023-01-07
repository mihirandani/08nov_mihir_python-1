
def  test (x,y):
    if x==y or abs(x+y)==5 or abs(x-y)==5 :
        return True

    else:
        return False


print(test(5,5))
print(test(10,5))
print(test(2,3))
print(test(5,10))
print(test(45,47))