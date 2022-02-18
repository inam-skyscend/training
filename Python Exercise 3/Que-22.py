# 22.Calculate your age in years, months and days.
from datetime import date
crt_dt=date.today()

birthdate=date(2001,4,1)

diff=crt_dt-birthdate
print("in Days:",diff.days)
print("Years",round(diff.days/365))
print("months:",round(diff.days/30))
#
# years = ((diff.total_seconds())/(365*24*3600))
# yearsInt=round(years)
#
# months=(years-yearsInt)*12
# monthsInt=int(months)
#
# days=(months-monthsInt)*(365.242/12)
# daysInt=int(days)
#
# print('You are {0} years, {1}  months, {2}  days'.format(yearsInt,monthsInt,daysInt))
#

# def age(birthdate):
#     today = date.today()
#     age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
#     return age
# print(age(birthdate))


