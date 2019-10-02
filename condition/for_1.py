str1 = input("Tell me a word: ")
str1=str1.upper()
a=input("which word you think press many times: ")
a=a.upper()
print (a)
list1=[]
for string in str1:
    list1.append(string)
print(list1)

#######

lt1=[]
count1 =len(list1)
print(count1)
for x in list1:
    if x==a.upper():
        #print(x)
        lt1.append(x)
    else:
        continue
print("Number of t in this string:", len(lt1))
    
