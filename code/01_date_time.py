# Simple program showing import operation and use of date and time
from datetime import datetime as dt

timenow = dt.now()
print("The current date and time is:", timenow)
print("The year is: ", dt.now().year)
print("The year is: ", dt.now().hour)
if 8 < dt.now().hour < 22:
    print("It is during work hours")
else:
    print("It is outside work hours")