from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
import os
os.system("clear")

print("=" * 50)
now = datetime.now()
today = date.today()
print(f"now       : {now}")
print(f"today     : {today}")
print("=" * 50)

# Use timedalta
yesterday = now + timedelta(days=-1)
last_week = now + timedelta(weeks=-1)
last_month = now + timedelta(days=-30)
last_year = now + timedelta(days=-365)
print(f"yesterday  : {yesterday}")
print(f"last week  : {last_week}")
print(f"last month : {last_month}")
print(f"last year  : {last_year}")
print("=" * 50)

# Use relativedelta
yesterday = now + relativedelta(days=-1)
last_week = now + relativedelta(weeks=-1)
last_month = now + relativedelta(months=-1)
last_year = now + relativedelta(years=-1)
print(f"yesterday  : {yesterday}")
print(f"last week  : {last_week}")
print(f"last month : {last_month}")
print(f"last year  : {last_year}")
print("=" * 50)