#**kwargs store the value as a dictionary
def my_kwargs(**kwargs):  
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print ('I did not find any fruit')

my_kwargs(fruit='apple')
print()
print()
def com_arg_kwarg(*args,**kwargs):
    print('*agrs store data as a tuppel:'+str(args))
    print()
    print('**kwagrs store data as a dictionary:'+str(kwargs))
    print()
    print("I have {} {}".format(args[0],kwargs['food']))

com_arg_kwarg(10,20,30,food='rice',work='code')