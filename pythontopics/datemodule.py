import datetime 
import os 
from os import name,system
from datetime import datetime, UTC
import pandas

time_now = datetime.datetime.now()
print("Current date and time: ", time_now)
timenow1 = datetime.now().time()
print("Current time: ", timenow1)

todaydate = datetime.date.today()

print(time_now.year)
print(time_now.month)
print(time_now.day)
print(time_now.hour)   
print(time_now.strftime("%d-%m-%Y"))
print(time_now.strftime("%d-%m-%Y %H:%M"))

