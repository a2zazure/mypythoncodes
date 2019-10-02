#Take input
y=int(input("Tell me a number:"))     #input value is always STRING.you need to change that value to int or float

#if-else in Python
x=10

if int(y)*x>=100:
    if int(y)*x==100:
        print('It is equal to 100')
    else:
        print("Ten times of you number", x*y, 'is greter then 100')
    #pass
else:
    print("Ten times of you number", x*y, 'is less then 100')
    #pass