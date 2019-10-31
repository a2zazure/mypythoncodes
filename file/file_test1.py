text =open("/home/share/Desktop/pytesting/file/test.txt",'a')
text.write('\nnow this is new1')
text.close()

file=open("/home/share/Desktop/pytesting/file/test.txt",'r')
x=file.readlines()
y=1
for line in x:
    if 'error' in line:
        print(y,':',line)
        y=y+1
file.close()
