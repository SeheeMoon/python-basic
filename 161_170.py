# 161

for x in range(0, 100):
    print(x)

# 162

for i in range(2002, 2051, 4):
    print(i)

# 163

for i in range(3, 31, 3):
    print(i)

# 164

for x in range (1, 100):
    print(99 - x)


# 165

for x in range(10):
    print(x / 10)

# 166

for i in range(1, 10):
    a = 3 * i
    print('3', 'x', i, '=', a)

# 167

for i in range(1, 10):
    a = 3 * i
    if a % 2 != 0:
        print('3', 'x', i, '=', a)

# num = 3
# for i in range(1, 10, 2) :
#     print (num, "x", i, " = ", num * i) range의 3번째 파라미터를 사용해서도 해결할 수 있음.

# 168

# lst = []
# for i in range(1, 11):
#     lst.append(i)

# sum_lst = sum(lst)
# print('합:', sum_lst)

hab = 0
for i in range(1, 11):
    hab += i
print ("합:", hab)  # hab 이라는 변수에 0을 저장하고, for 문을 통해 모든 값에 대해 누적합니다.

# 169

sum = 0
for i in range(1, 11):
    if i % 2 == 1:
        sum += i

print('합:', sum)

# 170

gop = 1
for i in range(2, 11):
    gop *= i

print('곱:', gop)