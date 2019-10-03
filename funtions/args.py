def myfun(a,b):
    return sum((a,b))*.05
#In this case if we give more then 2 value we will get error.
result1=myfun(40,60)
print(result1)


#to solve this issue we can use *agrs
def myagrs_fun(*args):          #args is just a word. we can use and name. but * is must
                                 #no * when calling
    for item in args:
        print (item)
    return sum(args) * 0.05


result2=myagrs_fun(40,60,100,30)
print('5'+'%'+' sum of your numbers: '+str(result2))
