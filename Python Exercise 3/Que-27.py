# 27.Get the 1st month of the current year from today's date.

from datetime import date

given_date = date.today()

first_month_of_year = given_date.replace(month=1)
str=first_month_of_year.strftime("%Y %B %d")

print("\nFirst month of year from today date: ", str, "\n")