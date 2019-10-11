class Testclass():
    def __init__(self,empname,emplast):
        self.empname=empname.capitalize()
        self.emplast=emplast.capitalize()
        self.empemail=empname+'.'+emplast+'@company.com'
x=input("emplye name: ")
y=input('employe lastname: ')
emp1_details=Testclass(x,y)
emp2_details=Testclass('mini','roy')
fileopen=open('emptest.txt','a')
fileopen.write('\nFirst Name: '+str(emp1_details.empname)+'\n Last Name: '+str(emp1_details.emplast)+'\n'+str(emp1_details.empemail))
fileopen.close()
print('NAME: '+str(emp1_details.empname)+'\n'+str(emp1_details.emplast)+'\n'+str(emp1_details.empemail))
