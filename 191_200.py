# 191

data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

commission = 0.014 / 100
for row in data:
    for col in row:
        print(col + col * commission)

# 192

for row in data:
    for col in row:
        print(col + col * commission)
    print('----')

# 193

result = []

for row in data:
    for col in row:
        result.append(col + col * commission)

print(result)

# 194

result = []

for row in data:
    lst = []
    for col in row:
        lst.append(col + col * commission)
    result.append(lst)

print(result) # 보조 리스트를 for문 안에 만들어야 한다.

# 195

ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for price in ohlc[1:]:
    for close in price[3:]:
        print(close)

# 196

for price in ohlc[1:]:
    for close in price[3:]:
        if close > 150:
            print(close)
        # else: # 이 부분은 있어도 되고 없어도 됨.
        #     continue

# 197

for price in ohlc[1:]:
    for close in price[3:]:
        if close >= price[0]:
            print(close)

# 198

volatility = []
for price in ohlc[1:]:
    vol = price[1] - price[2]
    volatility.append(vol)

print(volatility)

# 199

# for price in ohlc[3:]:
#     print(price[3] - price[0])

for price in ohlc[1:]:
    if price[3] > price[0]:
        print(price[1] - price[2])


# 200

sum = 0
for price in ohlc[1:]:
    sum += (price[3] - price[0])

print(sum)
