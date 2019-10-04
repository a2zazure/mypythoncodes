def tst_kwargs(*args,**kwargs):
    if 'food' in kwargs:
        print('You love {}'.format(kwargs['food']))
    else:
        print('No food in your list')
    return sum(args)
    

test=tst_kwargs(20,30,food='coke',love='walk')
print('result :{}'.format(test))

