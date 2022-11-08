# 121

# user = input('입력:')
# k = user.isupper()
# if k == True:
#     print(user.lower())
# else:
#     print(user.upper()) 

user = input("")
if user.lslower():
    print(user.upper())
else:
    print(user.lower()) # islower함수는 boolean을 반환하므로 이런 형식으로 바로 구문에 적용 가능하다.

# 122

score = input("입력:")
if 0 <= int(score) <= 20:
    print('E')
elif 20 < int(score) <= 40:
    print('D')
elif 40 < int(score) <= 60:
    print('C')
elif 60 < int(score) <= 80:
    print('B')
else: 
    print('A')

# 123 

user = input('입력:')
money = int(user[:-3])
money_type = user[-2:]
if money_type == '달러':
    print(money * 1167, '원')
elif money_type == '엔':
    print(money * 1.096, '원')
elif money_type == '유로':
    print(money * 1268, '원')
elif money_type == '위안':
    print(money * 171, '원')

