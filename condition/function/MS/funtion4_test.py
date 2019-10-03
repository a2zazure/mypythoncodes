def get_intitials(name):
    intitial=name[0:1].upper()
    return intitial

first_name=input('what is your name?\n')
first_name_int=get_intitials(first_name)

last_name=input('what is your name?\n')
last_name_int=get_intitials(last_name)
print(first_name_int +'.'+ last_name_int)

#directly call funtion in print statment
print("your initial is: " + get_intitials(first_name)+get_intitials(last_name))

