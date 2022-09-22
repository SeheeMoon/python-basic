# 자료형, 변수

name = "해피"
animal = "고양이"
age = 2
hobby = "낮잠"
is_adult = age >= 3

#print("우리집 " + animal + "의 이름은 " + name + "입니다.")
print(name + "는 " + str(age)  + "살이며, " + hobby + "을 아주 좋아해요.")
print(name + "는 어른일까요? " + str(is_adult))

'''
여러문장을
주석처리
할
수 
있습니다.'''

# Quiz 1
station = "인천공항"

print(station + "행 열차가 들어오고 있습니다.")

# 연산자
print(1+2)
print(4-1)
print(3*4)
print(8/2)

print(2**5) # 32
print(10%4) # 2
print(88//3) # 29

print(10 > 3) # True
print(3 >= 3) # True
print(24 < 10) # False

print(3 == 3)
print(4 == 7)
print(3 + 4 == 7)

print(3 != 2)
print(not(1 != 3))

print((3 > 1) and (3 < 5))
print((3 > 2) & (7 > 2))

print((2 > 3) or (7 > 3))
print((2 > 3) | (7 < 10))

print(3 < 5 <9)
print(3 < 10 < 1)

# 변수 활용
number = 4 + 3 * 3 # 13
print(number)
number += 4
print(number)
number *= 2
print(number)
number %= 7
print(number)

# 숫자처리함수
print(abs(-9)) # 절댓값
print(pow(5, 3)) # 제곱수
print(max(9,12)) # 최댓값
print(min(2,129)) # 최솟값
print(round(3.123123)) # 반올림

# 랜덤함수
from random import *
from unittest.mock import sentinel
print(random()) # 0.0 ~ 1.0 미만의 난수 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 난수 생성
print(int(random() * 10)) # 0 ~ 10 미만의 난수 생성
print(int(random() * 10) + 1) # 0 ~ 10 이하의 난수 생성 

# Quiz 2
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + " 일로 선정되었습니다.")

# 문자열
sentence = '안녕하세요'
print(sentence)
sentence2 = "저는 문세희입니다."
print(sentence2)
sentence3 = """
안녕하세요,
저는 문세희입니다.
"""
print(sentence3)

#슬라이싱
jumin = "011020-3234567"
if int(jumin[7]) == 3:
    print("성별: 남자")
else:
    print("성별: 여자")

print("연: " + jumin[0:2]) # 0 부터 2 직전까지 (0,1)
print("월: " + jumin[2:4])
print("일: " + jumin[4:6])

print("생년월일: " + jumin[:6]) # 처음부터 6 직전까지
print("뒤 7자리: " + jumin[7:]) # 7부터 끝까지
print("뒤 7자리 (뒤에부터): " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지

# 문자열처리함수
python = "Python is Amazing"
print(python.upper()) # 대문자로 출력
print(python.lower()) # 소문자로 출력

print(python[0].isupper()) # 해당 index 값이 대문자인지 확인
print(len(python)) # 문자열 길이 확인
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
print(python.index("n"))
print(python.index("n", index + 1)) # 두 번째 n이 있는 index값

print(python.find("Java")) # index는 해당 문자열이 없을 때 에러가 발생, find는 -1 출력
print(python.count("n")) # 해당 문자열이 몇 번 들어가있는지

# 문자열 포맷

# 방법 1
print("나는 %d살입니다." % 22)
print("나는 %s을 좋아해요" % "Python")
print("Apple은 %c로 시작합니다" % "A")

print("나는 %s살입니다." % 22) # %s는 모든 데이터타입을 읽을 수 있다.
print("나는 %s색과 %s색을 좋아합니다." % ("파란", "빨간")) # %뒤에 괄호로 여러 가지 데이터를 묶을 수 있음

# 방법 2
print("나는 {}살입니다.".format(22))
print("나는 {}색과 {}색을 좋아합니다.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아합니다.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아합니다.".format("파란", "빨간"))

# 방법 3
print("나는 {age}살이고, {color}색을 좋아합니다.".format(age = 22, color = "빨간"))
print("나는 {age}살이고, {color}색을 좋아합니다.".format(color = "파란", age = 22))

# 방법 4
age = 22
color = "노란"
print(f"나는 {color}색을 좋아하며, {age}살입니다.") # f는 앞의 값을 불러와서 쓴다는 뜻

# 탈출 문자
print("백문이 불여일견\n백견이 불여일타") # \n는 줄바꿈의 역할
print("저는 \"나도코딩\" 입니다.") # \"\", \'\'는 문장 내에서 ", '의 역할
print('저는 \'나도코딩\' 입니다.')
print("\\dfepple\\efwe\\wefwe\\wef") # \\는 문장 내에서 \역할

print("Red Apple\rPine") # \r은 커서를 맨 앞으로 이동
print("Redd\bApple") # \b는 백스페이스 역할
print("Red\tApple") # \t는 tab 역할

# Quiz 3

site = "https://naver.com"
code = site.replace("https://", "")
code2 = code[:code.index(".")]
code3 = code[:3]
key = code3 + str(len(code2)) + str(code.count("e")) + "!"
print("{0}의 비밀번호는 {1} 입니다.".format(site, key))

# 리스트
subway = [10, 20, 30]
print(subway)

print(subway.index(20))
subway.append("유재석")
print(subway)
print(subway.pop()) # 맨 뒤 값을 출력하고, 기존 list에서 해당 값을 없앰
print(subway)
print(subway.count(20))

num_list = [2, 5, 4, 1, 3]
num_list.sort()
print(num_list) 
num_list.reverse()
print(num_list)

mix_list = [2, True, "문세희"]
print(mix_list)

num_list.extend(mix_list)
print(num_list)

# 사전
cabinet = {3 : "유재석", 100 : "김태호"}
print(cabinet)
print(cabinet[100])
print(3 in cabinet)

cabinet[3] = "정형돈"
cabinet[4] = "노홍철"
print(cabinet)

cabinet2 = {"A-3" : "유재석", "B-100" : "김태호"}
cabinet2["C-3"] = "정준하"
print(cabinet2)
del cabinet2["C-3"]
print(cabinet2)

# 튜플 (리스트와 비슷하지만 내용 변경, 추가가 불가능하다.)
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])
# menu.add("생선까스") 추가가 불가능함.

(name, age, hobby) = ("김종국", 20, "코딩") # 여러 변수를 한 번에 설정할 수 있다.
print(name, age, hobby)

# 집합 (set)
my_set = {1, 2, 3, 3, 3}
print(my_set) # 중복과 순서가 없다.

java = {"유재석", "박명수", "하하"}
python = set(["유재석", "노홍철"])

print(java & python) # 교집합 출력방법
print(java.intersection(python))

print(java | python) # 합집합 출력방법
print(java.union(python))

print(java - python) # 차집합 출력방법
print(python - java)
print(java.difference(python))
print(python.difference(java))

java.add("길") # 집합 수정 가능
print(java)

java.remove("유재석")
print(java)

# Quiz 4
from random import * 
# id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17 ,18, 19, 20] # range(1, 21) 사용해서 자료구조 list로 변경하면 편리함
# shuffle(id)
# chicken = id[19]
# id.pop()
# coffee = sample(id, 3)

# print(""" -- 당첨자 발표 --
# 치킨 당첨자 : {}
# 커피 당첨자 : {}
# -- 축하합니다 --
# """.format(chicken, coffee))

users = range(1, 21)
users = list(users)
shuffle(users)
winner = sample(users, 4)

print("""-- 당첨자 발표 --
치킨 당첨자 : {}
커피 당첨자 : {}
-- 축하합니다 --
""".format(winner[0], winner[1:]))

# if

# weather = input("오늘 날씨는 어때요?")
# if weather == "비" or "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 착용하세요")
# else:
#     print("준비물 필요 없습니다")

# temp = int(input("오늘 기온은 어떻습니까?"))
# if temp > 30:
#     print("너무 덥습니다.")
# elif 10 < temp <= 30:
#     print("날씨가 좋습니다")
# elif 0 < temp <= 10:
#     print("외투를 챙기십시오")
# else:
#     print("너무 춥습니다.")

# for
# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#     print("{}, 커피가 준비되었습니다.".format(customer))

# # for waiting_no in [1, 2, 3, 4, 5]:
# for waiting_no in range(1, 6): # range로 범위도 설정 가능하다.
#     print("대기번호 {}번".format(waiting_no))

# # while
# customer = "토르"
# i = 5
# while i >= 1:
#     print("{}, 커피가 준비되었습니다. {}회 남았습니다.".format(customer, i))
#     i -= 1
#     if i == 0:
#         print("커피는 폐기되었습니다.")

# visitor = "아이언맨"
# i = 1
# while True:
#     print("{}, 커피가 {}번 째 준비되었습니다.".format(visitor, i))
#     i += 1

# customer = "토르"
# person = "Unknown"
# while person != customer:
#     print("{}, 커피가 준비되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?")
#     if person == "토르":
#         print("커피 받아가세요.")


# continue, break
# absent = [2, 5]
# no_book = [7]
# for student in range(1, 11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("수업은 여기까지, {}은 교무실로 따라와".format(student))
#         break
#     print("{}번, 책을 읽어라".format(student))



 # 한줄 for
people = [1, 2, 3, 4, 5]
people = [i+200 for i in people]
print(people)

# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)

students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)

# Quiz 5
from random import *
proper_time = range(5, 16)
proper_time = list(proper_time)
i = 0
for guest in range (1, 51):
    time = randrange(5, 51)
    if time in proper_time:
        print("[O] {}번째 손님 (소요시간 : {}분)".format(guest, time))
        i += 1
    else:
        print("[ ] {}번째 손님 (소요시간 : {}분)".format(guest, time))
print("총 탑승 승객 : {} 분".format(i))

print("안녕하세요")
        








