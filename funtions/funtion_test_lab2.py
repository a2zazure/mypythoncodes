#find 007 in a list
def spy_007(nums):
    list1=[0,0,7,'x']
    for num in nums:
        if num ==list1[0]:
            list1.pop(0)
    return len(list1)==1
    
jb=spy_007([1,0,0,7,7])
jb2=spy_007([0,0,2,7,8])
jb3=spy_007([1,6,0,7,6])
print(jb)
print(jb2)
print(jb3)