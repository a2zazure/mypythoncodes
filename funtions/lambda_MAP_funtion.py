def squar(num):
    return num**2
list1=[2,3,4,5]
for item in map(squar,list1):
    print(item)
print()
#OR
l2=list(map(squar,list1))
print(l2)
print()
print('#Not using MAP funtion')

def squar1(num):
    for item1 in num:
        print(item1**2)
list1=[2,3,4,5]
squar1(list1)

#############
#use lambda in map

t1=list(map(lambda num: num**2,list1))
print('output from lambda: '+str(t1))
