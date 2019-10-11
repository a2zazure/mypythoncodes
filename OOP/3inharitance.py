#INHARITANCE is the way to form a new classed using classes already been defined.

#here is base Class
class Animal():
    def __init__(self):
        print('ANIMAL CREATED')
    def name(self):
        print("This is animal")
    def eat(self):
        print("I am eating")
new_animal=Animal()
print(new_animal)

#now calling inharitaed the animal class in to Dog class
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog Create'.upper())
    def __str__(self):
        return f"hello"

print(Dog())

#here we can call the base class method also.
print(new_animal.eat())