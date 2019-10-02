#Dictionary in python
#It is colection of key:value pairs
mydic1 = {
    "ram":"Good",
    "sam":"my name",
    "age":36
}
print(mydic1)
#if we give the key as a input then it will show the value.
print(mydic1['ram']) #output will be Good which is value for ram

#we can change the value of a key from assine to a variable
mydic1['age']=50

#also we we can use this command for retrive the value
print(mydic1.get('age')) 
