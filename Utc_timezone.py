import datetime
import pytz

dt = datetime.datetime(2023,11,2,6,32,55, tzinfo=pytz.UTC)
print(dt)

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow) 
