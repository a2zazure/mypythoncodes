#def is for define a funtion ':' is must.
def funtion_name():
    print('hello world')

#RETURN send back the result of the funtion and also assine the output to a variable
def store_return(num1,num2):
    return num1+num2

#another use of return.
def dog_string(name):
        
    # if 'dog' in name:
    #     return True
    # else:
    #     return False
#we can replace replace if with return
    return 'dog' in name

#here calling the funtion in a pogram
funtion_name()
v1=input("tell me a number: ")
v2=input("tell me a number: ")
result=store_return(int(v1),int(v2))
print(result)

#dog string calling
result = dog_string("I have a cat")
print(result)