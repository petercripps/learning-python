# Simple program showing import operation and use of date and time
from datetime import datetime as dt

timenow = dt.now()
print("The current date and time is:",timenow)
print("The year is: ", timenow.year)
print("The time is: ", timenow.hour, ":", timenow.minute, ":", timenow.second)
if 8 < timenow.hour < 22:
    print("It is during work hours")
else:
    print("It is outside work hours")

date_str = '29/12/2017' # The date - 29 Dec 2017
format_str = '%d/%m/%Y' # The format
datetime_obj = dt.strptime(date_str, format_str)
print(datetime_obj.date())