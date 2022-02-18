# 24.Get the date which is 1 year from today's date.

import dateutil.relativedelta as rd
import datetime
crt_dt=datetime.date.today()
nextyear=crt_dt+rd.relativedelta(years=1)
print(nextyear)