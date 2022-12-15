# 291

f = open("/Users/seheemoon/Desktop/Pythonworkspace/매수종목1.txt", mode='wt', encoding='utf-8')
f.write("005930\n")
f.write("005380\n")
f.write("035420\n")
f.close()

# 292

f = open("/Users/seheemoon/Desktop/Pythonworkspace/매수종목2.txt", mode='wt', encoding='utf-8')
f.write("005930 삼성전자\n")
f.write("005380 현대차\n")
f.write("035420 NAVER\n")
f.close()

# 293

import csv

f = open("/Users/seheemoon/Desktop/Pythonworkspace/매수종목.csv", mode='w', encoding='cp949')
wr = csv.writer(f)
wr.writerow(["종목명", "종목코드", "PER"])
wr.writerow(["삼성전자", "005930", "15.79"])
wr.writerow(["NAVER", "035420", "55.82"])
f.close()

# 294

f = open("/Users/seheemoon/Desktop/Pythonworkspace/매수종목1.txt", 'r')
lst = []
lines = f.readlines()

for line in lines:
    code = line.strip()
    lst.append(code)

print(lst)
f.close()

# 295

f = open("/Users/seheemoon/Desktop/Pythonworkspace/매수종목2.txt", 'r')

key = []
value= []
lines = f.readlines()

for line in lines:
    strings = line.split()
    key.append(strings[0])
    value.append(strings[1])

dictionary = dict(zip(key, value))
print(dictionary)

# 296

per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)

# 297

per = ["10.31", "", "8.00"]
lst = []

for i in per:
    try:
        a = float(i)
    except:
        a = 0
    lst.append(a)
print(lst)

# 298

try:
    b = 3 / 0
except ZeroDivisionError:
    print("0으로 나누면 안되요")

# 299

data = [1, 2, 3]

for i in range(5):
    try:
        print(data[i])
    except IndexError as x:
        print(x)

# 300

per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)
    else:
        print("clean data")
    finally:
        print("변환 완료")

