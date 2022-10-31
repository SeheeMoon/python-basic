# 081

# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# scores.reverse()
# a, b, *valid_score = scores
# valid_score.reverse()
# print(valid_score)

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, _, _= scores
print(valid_score) # 언팩킹 시 좌측 여러개를 바인딩 할 때도 똑같이 적용하면 된다.

# 082

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_, _, *valid_score = scores
print(valid_score)

# 083

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_, *valid_score, _ = scores
print(valid_score)

# 084

temp = { }

# 085

ice = {'메로나': 1000, '폴라포': 1200, '빵빠레': 1800}
print(ice)

# 086

ice['죠스바'] = { 1200 }
ice['월드콘'] = { 1500 }
print(ice)

# 087

ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}

w = ice['메로나']

print("메로나 가격: {}".format(w))

# 088

ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}

ice['메로나'] = 1300
print(ice)

# 089

del(ice['메로나'])

# 090

# 딕셔너리에 없는 값으로 x
