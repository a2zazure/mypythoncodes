avg_cgpa=float(input('what is your avg CGPA?'))
lowest_cgpa=float(input('what is your lowest CGPA?'))

if avg_cgpa >= 90 and lowest_cgpa >= 70:
    result= True
else:
    result= False

if result:    #no details needed. results details already stored. 
    print("You are pass")