# 30.Get me the 1st and last date of the current month in the format as following. '14th June 2016 Tuesday 10:00:00 AM'

from datetime import datetime
import calendar

current_date = datetime.today()
print("current date: ", current_date)
print("first date of current month: ", current_date.replace(day=1).strftime("%dth %B %Y %A %H:%M:%S %p"))
month_data = calendar.monthrange(current_date.year, current_date.month)
print(month_data)
print("last date of current month: ", current_date.replace(day=month_data[1]).strftime("%dth %B %Y %A %H:%M:%S %p"))