# 131

과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
    print(변수)

# 과일 리스트에 저장된 변수들이 출력된다.

# 132

과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
  print("#####")

# for문의 핵심은 "들여쓰기된 코드가 자료구조에 저장된 데이터 개수만큼 반복된다"라고 설명했습니다. `과일 = ["사과", "귤", "수박"]` 에는 세 개의 데이터가 저장돼 있으므로 들여쓰기된 `print("####")`코드가 세 번 실행됩니다.

# 133

for 변수 in ["A", "B", "C"]:
  print(변수)

# alphabet = ["A", "B", "C"]
# for 변수 in alphabet:
#     print(변수)

변수 = "A"
print(변수)
변수 = "B"
print(변수)
변수 = "C"
print(변수) # 혹은

print("A")
print("B")
print("C")

# 134

for 변수 in ["A", "B", "C"]:
  print("출력:", 변수)

print('출력: A')
print('출력: B')
print('출력: C')

# 135

for 변수 in ["A", "B", "C"]:
  b = 변수.lower()
  print("변환:", b)

# print('변환:', 'A'.lower())
# print('변환:', 'B'.lower())
# print('변환:', 'C'.lower())

변수 = "A"
b = 변수.lower()
print("변환:", b)

변수 = "B"
b = 변수.lower()
print("변환:", b)

변수 = "C"
b = 변수.lower()
print("변환:", b)

# 136

변수 = 10
print(변수)
변수 = 20
print(변수)
변수 = 30
print(변수)

for 변수 in [10, 20, 30]:
    print(변수)

# 137

print(10)
print(20)
print(30)

변수 = 10
print(변수)
변수 = 20
print(변수)
변수 = 30
print(변수)

# 138

print(10)
print("-------")
print(20)
print("-------")
print(30)
print("-------")

for i in [10, 20, 30]:
    print(i)
    print("-------")


# 139

print("++++")
print(10)
print(20)
print(30)

print("++++")
for 변수 in [10, 20, 30]:
  print(변수)

# 140

print("-------")
print("-------")
print("-------")
print("-------")

for i in [10, 20, 30, 40]:
    print("-------")