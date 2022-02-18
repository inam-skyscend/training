# Get the date which is 1 week from today's date.

import datetime

crt_dt=datetime.date.today()
next_week = crt_dt+ datetime.timedelta(days=7)
print(next_week)