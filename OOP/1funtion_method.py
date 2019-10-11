class Sample():
    #class object attribute
    #SAME FOR ANY INSTANCE OF A CLASS
    species='mammal'
    def __init__(self,breed,name,spot=True):
        #Attributes
        #We take in the argument
        # Assigne it to self.attribute_name 
        self.breed=breed
        self.name=name
        #expect a boolean True/False
        self.spot=spot
        '''
        return 'Oho grate. You have a lab' breed=='lab'
            
        else:
            print('Okay. you have a ',breed)
        '''
my_sample=Sample(breed='lab',name='jony',spot=False)
print (my_sample.breed)
print (my_sample.spot)
print (my_sample.name)
print (my_sample.species.capitalize())
