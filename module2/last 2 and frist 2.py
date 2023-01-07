
def get_srting(text):
    if len (text)<2:
        return""

    return text[:2] +  text[-2:]


my_sring = input(" enter a string")
print("new modified string is:",get_srting(my_sring))
