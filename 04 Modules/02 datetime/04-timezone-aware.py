from datetime import datetime
from dateutil import tz
import os
os.system("clear")

## timezone
print("=" * 50)
time_local = datetime.now(tz.tzlocal())
time_utc = datetime.now(tz.UTC)

tz_tehran = tz.gettz("Asia/Tehran")
time_tehran = datetime.now(tz_tehran)

tz_toronto = tz.gettz("America/Toronto")
time_toronto = datetime.now(tz_toronto)

print(f"timezone Local   : time = {time_local}")
print(f"timezone Tehran  : time = {time_tehran}")
print(f"timezone UTC     : time = {time_utc}")
print(f"timezone Toronto : time = {time_toronto}")
print("=" * 50)
