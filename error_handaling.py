x=int(input('h'))
y=int(input('h'))

try:
    print(x/y)
except ZeroDivisionError as e:
    print('sorry nothing can devided by zero')
finally:
    print(x/y)
# finally:
#     print('x/y not possible')