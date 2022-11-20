# 181

apart = [['101호', '102호'], ['201호', '202호'], ['301호', '302호']]
print(apart)

# 182

stock = [["시가", 100, 200, 300], ["종가", 80, 210, 330]]
print(stock)

# 183

key = [100, 200, 300]
value = [80, 210, 330]
stock = {"시가": key, "종가": value}
print(stock)

# 184

key = ["10/10", "10/11"]
value = [80, 210, 330]

stock = {"10/10": [80, 110, 70, 90], "10/11": [210, 230, 190, 200]}
print(stock)

# 185

# apart = [ [101, 102], [201, 202], [301, 302] ]
# for i in range(len(apart)):
#     lst = apart[i]
#     print(lst[0], '호')
#     print(lst[1], '호')

apart = [ [101, 102], [201, 202], [301, 302] ]

for row in apart:
    for col in row:
        print(col, "호") # for 문 두개를 쓰면 간단하게 해결 가능

# 186

apart = [ [101, 102], [201, 202], [301, 302] ]

for row in reversed(apart):
    for col in row:
        print(col, '호')

# for row in apart[::-1]:
#     for col in row:
#         print(col, "호") # 인덱싱을 이용해서도 가능하다.

# 187

apart = [ [101, 102], [201, 202], [301, 302] ]

for row in reversed(apart):
    for col in reversed(row):
        print(col, '호')

# 188

apart = [ [101, 102], [201, 202], [301, 302] ]

for row in apart:
    for col in row:
        print(col, '호')
        print('-----')

# 189

apart = [ [101, 102], [201, 202], [301, 302] ]

for row in apart:
    for col in row:
        print(col, '호')
    print('-----')

# 190

apart = [ [101, 102], [201, 202], [301, 302] ]

for row in apart:
    for col in row:
        print(col, '호')
print('-----')

