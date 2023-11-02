import datetime

todaysDate = datetime.date.today()
print(todaysDate.day) # to just print today's day
print(todaysDate.weekday())
print(todaysDate.isoweekday())
tDelta = datetime.timedelta(days=7)
print(todaysDate + tDelta)