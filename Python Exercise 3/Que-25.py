# 25.Get the date which is 1 month from today's date.

from datetime import date
from dateutil.relativedelta import relativedelta

crt_dt=date.today()         #today date
print(crt_dt)

nextmonth=crt_dt+relativedelta(months=1)     #current date+1 month
print(nextmonth)

