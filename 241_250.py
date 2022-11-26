# 241

import datetime

now = datetime.datetime.now()
print(now)

# 242

print(type(now))

# 243

today = datetime.date.today()
lst = [5, 4, 3, 2, 1]
for x in lst:
    diff_days = datetime.timedelta(days=x)
    previous_day = today - diff_days
    print(previous_day)

# 244

print(now.strftime('%H:%M:%S'))

# 245

from datetime import datetime

print(datetime.strptime("2020-05-04", "%Y-%m-%d"))
print(type(datetime.strptime("2020-05-04", "%Y-%m-%d")))

# 246
import datetime
import time

for i in range(10):
    now = datetime.datetime.now()
    print(now.strftime('%H:%M:%S'))
    time.sleep(1)

# 247

