a1=input("Tell me line.\n")
a2=input("which letter you want to search?")
list1=[]
for item in a1:
    list1.append(item)
print(list1)
list2=[]
for item2 in list1:
    if item2==a2:
       list2.append(item2)
    else:
        continue
print (list2)
    