from datetime import datetime
birthday= input('when is your birthday (dd/mm/yyyy)? ')

birthday_date= datetime.strptime(birthday, "%d/%m/%Y")
print('Your birthday is '+str(birthday_date))
