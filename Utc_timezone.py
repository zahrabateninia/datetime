import datetime
import pytz

dt = datetime.datetime(2023,11,2,6,32,55, tzinfo=pytz.UTC)
# dt_now = datetime.datetime.now() # we can add a timezone 
# dt_utcnow = datetime.datetime.utcnow() # current UTC time but the TZ info is still set to none