import datetime
todaysDate = datetime.date.today()
my_birthday = datetime.date(2024,8,28)
till_birthday = my_birthday - todaysDate
print(till_birthday.days) 
print(till_birthday.total_seconds())