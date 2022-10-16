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

# 표준입출력

print("Python", "Java", sep = ",", end="?")

import sys
print("Python", "Java", file = sys.stdout)
print("Python", "Java", file = sys.stderr)

scores = {'수학':0, '영어':50, '코딩':100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")

for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))

# 표준입력
# answer = input("아무값이나 입력하세요 : ") # 여기서 입력된 값은 항상 문자열 형태로 저장
# print("입력값은 " + answer + "입니다.")

# 다양한 출력 포맷

print("{0: >10}".format(500)) # 빈 공간은 빈 공간으로, 오른쪽 정렬, 10칸 확보
print("{0:_<+10}".format(-500)) # 부호까지 붙이기
print("{0: >30,}".format(10000000000000)) # 세 자릿수 마다 ,로 구분
print("{0:^<+20,}".format(10304022304))
print("{0:f}".format(5/3)) # 소수점 출력
print("{0:.2f}".format(5/3)) # 소수점 둘째자리까지 출력 (셋째 자리에서 반올림)

# 파일 입출력
# score_file = open("score.txt", "w", encoding = "utf8") # "w"는 write(읽기) 전용, 덮어쓰기
# print("수학 : 0", file = score_file)
# print("영어 : 0", file = score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 90")
# score_file.close()

# score_file = open("score.txt", 'r', encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", 'r', encoding="utf8")
# print(score_file.readline(), end = "") # 한 줄씩 불러오고, 커서는 다음 줄로 이동
# print(score_file.readline(), end = "") 
# print(score_file.readline(), end = "") 
# print(score_file.readline(), end = "") 
# score_file.close()

# score_file = open("score.txt", 'r', encoding="utf8") # 파일이 몇 줄인지 모를 때
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# score_file = open("score.txt", 'r', encoding="utf8")
# lines = score_file.readlines() # list 형태로 저장
# for line in lines:
#     print(line, end="")
# score_file.close()

# pickle : 프로그램 상에서 데이터를 파일 형태로 저장

# import pickle
# # profile_file = open("profile.pickle", "wb")
# # profile = {"이름": "박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# # print(profile)
# # pickle.dump(profile, profile_file) # profile의 정보를 file에 저장
# # profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) # file의 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

# with

# import pickle
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요.")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read()) 

# Quiz 7

for num in range (1, 51):
    with open("{}주차.txt".format(num), "w", encoding="utf8") as report_file:
        report_file.write("- {} 주차 주간보고 -\n부서 :\n이름 :\n업무 요약 :".format(num))


        