from datetime import date, time, datetime
import os
os.system("clear")
"""
Important Note: strftime() stands for string format time

  -time.strftime()     -> convert time     object to string
  -date.strftime()     -> convert date     object to string
  -datetime.strftime() -> convert datetime object to string

All above methods return a string type, so you can't use it in arithmetics.
"""

print("Using 'time', 'date' and 'datetime': ")
date1 = date(year=2023, month=4, day=10)
time1 = time(hour=8, minute=20, second=30)
datetime1 = datetime(2023, 4, 10, 8, 20, 30)
print(f'{date1}          formatted: {date1.strftime("date=%Y/%m/%d")}')
print(f'{time1}            formatted: {time1.strftime("time=%H:%M")}')
print(f'{datetime1} formatted: {datetime1.strftime("date=%Y/%m/%d time=%H:%M")}')
print("=" * 50)

now = datetime.now()
today = date.today()
current_time = time(now.hour, now.minute, now.second)
print(f"now          = {now}")
print(f"current time = {current_time}")
print(f"today        = {today}")
print("=" * 50)

birthday = datetime(year=2024, month=2, day=24)
print(f"remainig to birthday: {birthday - now}")
print("=" * 50)





