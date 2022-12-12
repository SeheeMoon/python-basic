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
# import datetime
# import time

# for i in range(10):
#     now = datetime.datetime.now()
#     print(now.strftime('%H:%M:%S'))
#     time.sleep(1)

# 247

# 1) import 모듈명 해서 임포트하는 방법 : 모듈 내의 변수를 사용하기 위해서는 모듈.변수의 형식으로 계속 써주어야 한다.
# 2) from 패키지 import 모듈명 해서 임포트하는 방법 : 변수만 입력해서 사용가능.
# 3) from 패키지 import 모듈명 as 별칭명
# 4) import 패키지.모듈명

# 248

import os
print(os.getcwd())


# 249

# src = "practice.txt"
# os.rename(src, 'dst.txt')

# 250

import numpy as np

a = np.arange(0.1, 0.6, 0.1)
print((list(a), 1))
