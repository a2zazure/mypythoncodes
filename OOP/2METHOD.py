class sample2():
    species='mammal'
    def __init__(self,name,breed,spot=False):
        self.name=name
        self.breed=breed
        self.spot=spot
    #Action/Oparation. ----> Methopd. 
    # This act same like a funtion.
    def bark(self,number):
        #here no need to apply the self.number. becase it is not a part of instance of a class(__init__). 
        # And get details from user.
        print('WOOF!!! My name is {}. And the number is {}'.format(self.name,number))

my_dog=sample2(name='jony',breed='lab')
print(my_dog.name)
print(my_dog.breed)
print(my_dog.spot)
print(my_dog.species)
print(my_dog.bark(10))

