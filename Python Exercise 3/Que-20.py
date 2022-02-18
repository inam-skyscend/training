from datetime import datetime

crnt_dt=datetime.now()
print(crnt_dt)

str_dt=crnt_dt.strftime("%d %B  %Y,%A %H:%M:%S")
print(str_dt)
