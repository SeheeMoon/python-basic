# 231

# def n_plus_1 (n) :
#     result = n + 1

# n_plus_1(3)
# print (result) # 함수 내부에서 계산한 값(지정한 변수)를 외부에 전달하기 위해서는 return을 사용해야 한다.

# 232

def make_url(str):
    url = "www." + str + ".com"
    return url

make_url("naver")

# 233

def make_list(str):
    lst = []
    for i in range(len(str)):
        lst.append(str[i])
    print(lst)

make_list("abcd")

def make_list (string) :
    my_list = []
    for 변수 in string :
        my_list.append(변수)
    return my_list # for 구문에서 string을 범주로 지정할 수도 있다.

def make_list (string) :
    return list(string) # 리스트 함수로도 가능

# 234

def pickup_even(num_list):
    lst = []
    for x in num_list:
        if x % 2 == 0:
            lst.append(x)
    print(lst)

pickup_even([3, 4, 5, 6, 7 ,8])

# 235

def convert_int(num_str):
    num = int(num_str.replace(',', ''))
    print(num)

convert_int("1,234,567")

# 236

def 함수(num) :
    return num + 4

a = 함수(10)
b = 함수(a)
c = 함수(b)
print(c) # 22

# 237

def 함수(num) :
    return num + 4

c = 함수(함수(함수(10)))
print(c) # 22

# 238

def 함수1(num) :
    return num + 4

def 함수2(num) :
    return num * 10

a = 함수1(10)
c = 함수2(a)
print(c) # 140

# 239

def 함수1(num) :
    return num + 4

def 함수2(num) :
    num = num + 2
    return 함수1(num)

c = 함수2(10)
print(c) # 16

# 240

def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c) # 28



