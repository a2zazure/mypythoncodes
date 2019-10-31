import csv

with open('/home/share/Desktop/pytesting/file/us-500.csv','r') as csv_file:
    #before do anything need store data into csv.reader file.
    csv_reader=csv.reader(csv_file)

    next(csv_reader) #it will remove first line and output only show the values. 

#['first_name', 'last_name', 'company_name', 'address', 'city', 'county', 'state', 'zip', 'phone1', 'phone2', 'email', 'web']
    for line in csv_reader:
        #print(line) will print all details. But we can filter as well with index.
        #like first_name index 0 and company_name is 2
        print(line[0],' ',line[5])
