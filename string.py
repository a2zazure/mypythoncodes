first_name=input("First Name: ").capitalize()
last_name=input("last Name: ").capitalize()
output ='hello, ' +first_name + ' '+last_name
print(output)
output ='hello, {} {}'.format(first_name, last_name).upper()
print(output)
# the space between 2 {} {} is showing this output as well.
output ='hello, {1} {0}'.format(first_name, last_name) 
print(output)
output=f'hello {first_name} {last_name}' #only PYTHON has this feture
print(output)
