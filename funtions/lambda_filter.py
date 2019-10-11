def even_search(num):
    return num%2 ==0
number=[1,2,3,4,5,6,7,8]

#Fileter do the filter out as per funtion declair.
# here from the list 1-8 filter the even numbers.  
num_col=list(filter(even_search,number))
print(num_col)

#lambda use filter
num_col2=list(filter(lambda num1 : num1%2 == 0,number))
print('Output from lambda Filte: '+str(num_col2))

