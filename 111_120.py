# 111

print(input("")*2)

# 112

num = input("입력")
print(int(num) + 10)

# 113
num = int(input('입력'))
if num % 2 == 1:
    print('홀수')
else:
    print('짝수')

# 114

num = int(input('입력'))
if num + 20 > 255:
    print(255)
else:
    print(num + 20)

# 115

user = input("입력값: ")
num = int(user) - 20
if num < 0:
    print(0)
elif num > 255:
    print(255)
else:
    print(num)

# 116

user = str(input("현재시간: "))
if user[-2:] == "00":
    print("정각 입니다.")
else:
    print("정각이 아닙니다.") # str은 & 연산자 사용 불가.

# 117

fruit = ["사과", "포도", "홍시"]
user = input('좋아하는 과일은?: ')
if user in fruit:
    print('정답입니다.')
else:
    print('오답입니다.')

# 118

warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
user = input('입력: ')
if user in warn_investment_list:
    print('투자 경고 종목입니다')
else:
    print('투자 경고 종목이 아닙니다')

# 119

fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
season = input("제가좋아하는계절은: ")
if season in fruit:
    print("정답입니다.")
else:
    print("오답입니다.") # 딕셔너리의 key값에 포함되어 있는 값을 지정할 필요는 따로 없다.

# 120

fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input('좋아하는과일은? ')
if user in fruit.values():
    print('정답입니다.')
else:
    print('오답입니다.') # 딕셔너리의 value 값에 포함되어 있는 값을 지정할 때는 values.()함수를 이용한다.