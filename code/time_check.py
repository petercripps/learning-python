# Use date and time to check if within working hours.

from datetime import datetime as dt
start_hour = 8
end_hour = 22

def working_hours(now_hour):
    if start_hour < now_hour < end_hour:
        return True   
    else:
        return False
        

if working_hours(dt.now().hour):
    print("It is during work hours")
else:
    print("It is outside work hours")