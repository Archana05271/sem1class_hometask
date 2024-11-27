#Example 5: Iterating over the days of a month
import calendar
# Input year and month
year = 2024
month = 10
# Iterate over the days of the month
for day in calendar.calendar().itermonthdays(year, month):

    print(day)
