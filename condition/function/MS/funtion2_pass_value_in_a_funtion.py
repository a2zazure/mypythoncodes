from datetime import datetime

#create a funtion where first print message need to put in a script

def print_time (task_name):
    print(task_name)
    print(datetime.now())

print_time('Loop start time'.upper())
for x in range(0,5):
    print (x)
print_time('Loop stop time')