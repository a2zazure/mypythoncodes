'''
def print2(string1):
    for item in string1:
        print (item,'X 2=',item*2)
        
l2=[1,2,3]
print2(l2)
'''
def table1(val1):
    for item in range(1,11):
        print(val1,'x',item,' = ',val1*item)

x=int(input("which table do you want: "))
table1(x)