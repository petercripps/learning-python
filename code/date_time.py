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