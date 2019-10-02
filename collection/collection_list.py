#python collection (Arrays)
'''
there are 4 types of collection in Python.
1. list  [use same value also in a list]
2. Tupel [same as list.but cant change the value in Tuple]
3. set [unorder and unindex and no same value, well defined object]
4. Dictionary [with key value pair]
'''
l1 = [2,4,65,7,4] #[] is use for list
print ('print my first list is:', l1)
#indexing in Python
print ('print my first number in that list is :', l1[0]) #count starts with 0
print ('print my 4th number in that list is :', l1[3]) #count starts with 0

#add aliment in the list
l1.append(524)
print ('print my changed first list is:', l1)
#change value
l1[5]= 65
#remove aliment in the list
l1.pop(1) #here value is reffer to INDEX number
print ('print my changed first list is:', l1)
l1.remove(4) #here value is list VALUE. search and delete.
print ('print my changed first list is:', l1)

#clear list
l1.clear()
print ('print my changed first list is:', l1)

#list can hold int string and flout or list
l2=[2,'test',[2,4,5]]
print('print list2', l2)
print('print index2 from inside list2', l2[2][2])