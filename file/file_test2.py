f= open("/home/share/Desktop/pytesting/file/test.txt")
w=open("/home/share/Desktop/pytesting/file/test2.txt",'a')
for line in f:
    if 'error' in line:
        print (line)
        w.write(line)
