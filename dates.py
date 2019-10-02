# to get current date and Time
# we need to use the DATETIME libary

from datetime import datetime

current_date= datetime.now()
# The now funtion returns current date time object
print('Today is '+ str(current_date))

#TimeDelta funtion is used to define a period of time.
from datetime import datetime,timedelta
one_day=timedelta(days=1)
yesterday=current_date-one_day
tomorrow=current_date+one_day
print('Yesterday was '+str(yesterday.day)+"/"+ str(yesterday.month)+"/"+str(yesterday.year))

#use date function to control date format
print('Tomorrow is '+str(tomorrow.day)+"/"+ str(tomorrow.month)+"/"+str(tomorrow.year))

one_week =timedelta(weeks=1)
last_week=current_date-one_week
print('last week was '+str(last_week))