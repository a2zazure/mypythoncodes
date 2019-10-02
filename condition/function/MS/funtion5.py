#Funtion can accept multiple parameter. And you can provide default value also
def get_init (name,init_upper=True):
    if init_upper:
        initials=name[0:1].upper()
    else:
        initials=name[0:1]
    return initials

first_name=input('enter your first name: ')
first_name_init=get_init(first_name,False)
print(first_name_init)

#Here no 2nd parameter is given as an input. this time by default it will be TRue and upper case will show
last_name=input('enter your last name: ')
last_name_init=get_init(last_name)
print(last_name_init)
