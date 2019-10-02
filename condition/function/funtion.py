def listprint(list1,greet):
    CRED = '\033[91m'
    CEND = '\033[0m'
    print(CRED +greet.upper()+ CEND)
    for item in list1:
        if item=='ram':
            
            print('This is not fruit'.upper())
            continue
        print ("value of this item is:",item.upper())

list1=['apple','ram','sham']
a=('a','b','c')

listprint (list1,"Welcome to funtion world")
listprint (a,"Welcome to funtion world")