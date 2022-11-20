# 171

price_list = [32100, 32150, 32000, 32500]

# for x in price_list:
#     print(x)

for i in range(len(price_list)):
    print(price_list[i]) # range를 사용하려면 인덱싱과 len()함수를 사용한다.

# 172

# price_list = [32100, 32150, 32000, 32500]

# for x in range(len(price_list)):
#     print(x, price_list[x])

price_list = [32100, 32150, 32000, 32500]
for i, data in enumerate(price_list):
    print(i, data) # 파이썬의 내장함수인 enumerate()함수를 이용하면 인덱스와 원소를 동시에 접근하면서 루프를 돌릴 수 있다.

# 173

price_list = [32100, 32150, 32000, 32500]

for i in range(len(price_list)):
    print(len(price_list) - 1 - i, price_list[i])

# 174

price_list = [32100, 32150, 32000, 32500]
x = 100
for i in range(1, len(price_list)):
    print(x, price_list[i])
    x += 10

# 175

my_list = ["가", "나", "다", "라"]
for i in range(len(my_list)):
    if i <= 2:
        print(my_list[i], my_list[i + 1])
    if i > 2:
        break

# 176

my_list = ["가", "나", "다", "라", "마"]
for i in range(len(my_list) - 2):
    print(my_list[i], my_list[i + 1],  my_list[i + 2])

# 177

my_list = ["가", "나", "다", "라"]

for i in range(len(my_list) - 1):
    print(my_list[3 - i], my_list[2 - i])

# 178

my_list = [100, 200, 400, 800]

for i in range(len(my_list) - 1):
    print(my_list[i + 1] - my_list[i])

# 179

my_list = [100, 200, 400, 800, 1000, 1300]

for i in range(len(my_list) - 2):
    print(sum(my_list[i:i + 3]) / len(my_list[i:i + 3]))

# 180

low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

volatility = []

for i in range(len(low_prices)):
    vol = high_prices[i] - low_prices[i]
    volatility.append(vol)

print(volatility)