# 21.Get the difference between two dates in days.

from datetime import date as dt
crt_dt=dt.today()
print(crt_dt)

new_dt=dt(2021,8,15)
print(new_dt)

diff=crt_dt-new_dt
print(diff)
