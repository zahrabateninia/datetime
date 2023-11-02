import datetime

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now() # we can add a timezone 
dt_utcnow = datetime.datetime.utcnow() # current UTC time but the TZ info is still set to none

print(dt_today) # current local date time with a timezone of none

print(dt_now) 

print(dt_utcnow)