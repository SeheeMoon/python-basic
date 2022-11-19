# 151

리스트 = [3, -20, -3, 44]

for x in 리스트:
    if x < 0:
        print(x)


# 152

리스트 = [3, 100, 23, 44]

for x in 리스트:
    if x % 3 == 0:
        print(x)

# 153

리스트 = [13, 21, 12, 14, 30, 18]

for x in 리스트:
    if x % 3 == 0 and x < 20:
        print(x) # 코드의 가독성 향상을 위해선 괄호를 넣는 것도 도움이 된다.

# 154

리스트 = ["I", "study", "python", "language", "!"]

for x in 리스트:
    y = len(x)
    if y >= 3:
        print(x)

# 155

리스트 = ["A", "b", "c", "D"]

# for x in 리스트:
#     y = x.isupper()
#     if y == True:
#         print(x)

for 변수 in 리스트:
  if 변수.isupper():
    print(변수) # 이 때 바로 True값에 해당하는 결과로 진행할 수 있음.

# 156

리스트 = ["A", "b", "c", "D"]

# for x in 리스트:
#     y = x.isupper()
#     if y == False:
#         print(x)

    
리스트 = ["A", "b", "c", "D"]
for 변수 in 리스트:
  if not 변수.isupper():
    print(변수) # not 연산자로도 가능

# 157

리스트 = ['dog', 'cat', 'parrot']
for x in 리스트:
    y = x[0].upper()
    print(y + x[1:])

# 158

리스트 = ['hello.py', 'ex01.py', 'intro.hwp']

for x in 리스트:
    y = x.split('.')[0]
    print(y)

# 159

리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for x in 리스트:
    y = x.split('.')[1][0]
    if y == 'h':
        print(x)

# 160

리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']

for x in 리스트:
    y = x.split('.')[1][0]
    if y == 'h' or y == 'c':
        print(x)