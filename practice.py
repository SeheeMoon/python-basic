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
