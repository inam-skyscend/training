# 29. Get the first date and last date of the current month.

from datetime import date
import calendar

current_date = date.today()
print("current date: ", current_date)
print("first date of current month: ", current_date.replace(day=1))
month_data = calendar.monthrange(current_date.year, current_date.month)
print(month_data)
print("last date of current month: ", current_date.replace(day=month_data[1]))