# 함수

def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()

# 반환값을 받는 함수

def deposit(balance, money): # 입금
    print("입금이 완료되었습니다. 잔액은 {} 원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money): # 출금
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {} 원입니다.".format(balance))
        return balance

def night_withdraw(balance, money): # 저녁에 출금
    commission = 100
    return commission, balance - money - commission



balance = 0
balance = deposit(balance, 1000)
# balance = withdraw(balance, 500)
commission, balance = night_withdraw(balance, 500)
print("출금이 완료되었습니다. 수수료는 {} 원이며, 잔액은 {} 원입니다.".format(commission, balance))

# 함수의 기본값

def profile(name, age = 17, main_lang = "python"):
    print("이름 : {} \t나이 : {} \t주 사용언어 : {}".format(name, age, main_lang))

profile("유재석")

# 키워드로 함수 호출

def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(main_lang = "Java", name = "david", age = 29)

# 가변인자를 이용한 함수 호출

def profile(name, age, *language):
    print("이름 : {} \t나이 : {} \t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 17, "python", "java", "c#", "C", "c++")
profile("김태호", 23, "flutter", "node.js", "django")

# 전역 변수와 지역 변수

gun = 10

def checkpoint(soldiers):
    global gun
    gun = gun - soldiers
    print("[함수 내] 남은 총: {}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {}".format(gun))
    return gun

print("전체 총 : {}".format(gun))
# checkpoint(2)
gun = checkpoint_ret(gun, 2)
print("남은 총 : {}".format(gun))

# Quiz 6

# def std_weight(height, gender):
#     if gender == "남자":
#         key = round(height**2/10000*22, 2)
#         print("키 {}cm 남자의 표준 체중은 {}kg 입니다.".format(height, key))
#     else:
#         key = round(height**2/10000*21, 2)
#         print("키 {}cm 여자의 표준 체중은 {}kg 입니다.".format(height, key))

# std_weight(162, "여자")
# std_weight(178, "남자")

def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 162
gender = "여자"
weight = round(std_weight(height / 100, gender), 2)

print("키 {}cm {}의 표준 체중은 {}kg 입니다.".format(height, gender, weight))

