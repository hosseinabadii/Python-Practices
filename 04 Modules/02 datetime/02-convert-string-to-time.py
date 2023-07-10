from datetime import date, time, datetime
from dateutil import parser
from dateutil.relativedelta import relativedelta
import os
os.system("clear")
"""
Important Note: strptime() stands for string parse time

  datetime.strptime()  -> convert a string to a datetime object

So you can use it in arithmetics.
"""

print("=" * 50)
print("CONVERTING STRING TO DATETIME, DATE, TIME:")
print("=" * 50)

print("\n1.Using datetime.strptime()")
dt1 = datetime.strptime("2004--10--1", "%Y--%m--%d")
print("dt1=", dt1)
dt2 = datetime.strptime("2014 12 21", "%Y %m %d")
print("dt2=", dt2)
print(f"difference between dt1 and dt2 {dt2-dt1}")
print(f"difference between dt1 and dt2 {relativedelta(dt2, dt1)}")
print("=" * 50)


print("\n2.Using parser.parse()")
now = datetime.now()
birthday = parser.parse("2024 2 24")
print(f"your birthday: {birthday}")
print(f"remainig to birthday: {birthday - now}")
print(f"remainig to birthday: {relativedelta(birthday, now)}")
print("=" * 50)


print("\n3.Using fromisoformat()")
print("time    =", time.fromisoformat("20:25:40"))
print("date    =", date.fromisoformat("2023-04-10"))
print("datetime=", datetime.fromisoformat("2023-04-10 20:25:40"))
print("=" * 50)

