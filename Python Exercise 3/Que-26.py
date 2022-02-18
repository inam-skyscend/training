# 26.Get the 1st day of the current month from today's date.' \
from datetime import date

given_date = date.today()

first_day_of_month = given_date.replace(day=1)

print("\nFirst day of month: ", first_day_of_month, "\n")
