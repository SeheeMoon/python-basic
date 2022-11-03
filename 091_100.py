# 091

inventory = {'메로나' : [300, 20], '비비빅' : [400, 3], '죠스바': [250, 100]}
# 딕셔너리의 값이 두 개 이상일 때 리스트로 감싸준다.

# 092

print(inventory['메로나'][0], '원') # 딕셔너리 인덱싱

# 093

print(inventory['메로나'][1], '개')

# 094

inventory['월드콘'] = [500,7]
print(inventory) # 딕셔너리에 값 추가

# 095

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice_key = list(icecream.keys())
print(ice_key)

# 096

ice_value = list(icecream.values())
print(ice_value)

# 097

print(sum(ice_value))

# 098

new_product = {'팥빙수':2700, '아맛나':1000}

icecream.update(new_product)
print(icecream)

# 099

keys = ("apple", "pear", "peach")
vals = (300, 250, 400)

result = dict(zip(keys, vals))
print(result)

# 100

date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]

close_table = dict(zip(date, close_price))
print(close_table)
