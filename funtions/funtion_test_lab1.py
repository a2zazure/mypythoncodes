#reverce evry word in a text
def rword(test):
    list1=test.split()
    list2=[]
    for item in list1:
        list2.append(item[::-1])
    return ' '.join(list2)

rw=rword("hello wold")
print(rw)
