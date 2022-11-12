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

# user = input('입력:')
# money = int(user[:-3])
# money_type = user[-2:]
# if money_type == '달러':
#     print(money * 1167, '원')
# elif money_type == '엔':
#     print(money * 1.096, '원')
# elif money_type == '유로':
#     print(money * 1268, '원')
# elif money_type == '위안':
#     print(money * 171, '원')

환율 = {"달러": 1167, 
        "엔": 1.096, 
        "유로": 1268, 
        "위안": 171}
user = input("입력: ")
num, currency = user.split()
print(float(num) * 환율[currency], "원") # # 딕셔너리와 split함수를 이용하여 작성

# 124

user1 = int(input('number1: '))
user2 = int(input('number2: '))
user3 = int(input('number3: '))

if user1 > user2 >= user3 or user1 > user3 >= user2:
    print(user1)
elif user2 > user1 >= user3 or user2 > user3 >= user1:
    print(user2)
else:
    print(user3)

# 125

# 번호 = {"SKT": "011", "KT": "016", "LGU": "019", "알수없음": "010"}
# user = input("휴대전화 번호 입력: ")
# if user[:3] == "011":
#     print("당신은 SKT 사용자입니다.")
# elif user[:3] == "016":
#     print("당신은 KT 사용자입니다.")
# elif user[:3] == "019":
#     print("당신은 LGU 사용자입니다.")
# else:
#     print('알 수 없음')

number = input("휴대전화 번호 입력: ")
num = number.split("-")[0]
if num == "011":
    com = "SKT"
elif num == "016":
    com = "KT"
elif num == "019":
    com = "LGU"
else:
    com = "알수없음"
print(f"당신은 {com} 사용자입니다.")

# 126

우편번호 = input("우편번호: ")
우편번호 = 우편번호[:3]
if 우편번호 in ["010", "011", "012"]:
    print("강북구")
elif 우편번호 in ["014", "015", "016"]:
    print("도봉구")
else:
    print("노원구") # if 문과 리스트를 사용하여 조건문 만들기

# 127

user = input('주민등록번호: ')
# print(user[7])
if user[7] == '1' or user[7] == '3':
    print('남자')
else:
    print('여자')

# 128

seoul = ['01', '02', '03', '04', '05', '06', '07', '08']
user = input('주민등록번호: ')
user = user.split('-')[1]
region = user[1:3]
if region in seoul:
    print('서울 입니다.')
else:
    print('서울이 아닙니다.')

# 129

user = input('주민등록번호: ')
num1 = list(user.split('-')[0])
num2 = list(user.split('-')[1])
num3 = num1 + num2
num = list(map(int, num3))
valid_num = str(num[12])
key = str(11 - ((num[0] * 2 + num[1] * 3 + num[2] * 4 + num[3] * 5 + num[4] * 6 + num[5] * 7 + num[6] * 8 + num[7] * 9 + num[8] * 2 + num[9] * 3 + num[10] * 4 + num[11] * 5) % 11))
if key[-1] == valid_num:
    print('유효한 주민등록번호입니다.')
else:
    print('유효하지 않은 주민등록번호입니다.')

# num = input("주민등록번호: ")
# 계산1 = int(num[0]) * 2 + int(num[1]) * 3 + int(num[2]) * 4 + int(num[3]) * 5 + int(num[4]) * 6 + \
#         int(num[5]) * 7 + int(num[7]) * 8 + int(num[8]) * 9 + int(num[9]) * 2 + int(num[10])* 3 + \
#         int(num[11])* 4 + int(num[12]) * 5
# 계산2 = 11 - (계산1 % 11)
# 계산3 = str(계산2)

# if num[-1] == 계산3[-1]:
#     print("유효한 주민등록번호입니다.")
# else:
#     print("유효하지 않은 주민등록번호입니다.")

# 130
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

시가 = float(btc['opening_price'])
종가 = float(btc['closing_price'])
최고가 = float(btc['max_price'])
최저가 = float(btc['min_price'])

변동폭 = 최고가 - 최저가

if 시가 + 변동폭 > 최고가:
    print('상승장')
else:
    print('하락장')