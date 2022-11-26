# 221

# def print_reverse(str):
#     print(reversed(str))

# print_reverse("python") # # reversed는 문자열 x

def print_reverse(str):
    print(str[::-1])

print_reverse("python")

# 222

def print_score(score_list):
    mean = sum(score_list) / len(score_list)
    print(mean)

print_score ([1, 2, 3])

# 223

def print_even(num_list):
    for x in num_list:
        if x % 2 == 0:
            print(x)
        else: 
            continue # 이 부분 굳이 안 써도 됨.

print_even ([1, 3, 2, 10, 12, 11, 15])

# 224

def print_keys(dic):
    for key in dic.keys():
        print(key)

print_keys ({"이름":"김말똥", "나이":30, "성별":0})

# 225

my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}

def print_value_by_key(my_dict, key):
    print(my_dict[key])

print_value_by_key(my_dict, "10/26") # 딕셔너리 관련 함수 숙지 필요

# 226

def print_5xn(string):
    for i in range(int(len(string) / 5 + 1)):
        str = string[i * 5: i * 5 + 5]
        print(str)

print_5xn("아이엠어보이유알어걸나나나")

# 227

def print_mxn(string, m):
    for i in range(int(len(string) / m + 1)):
        str = string[i * m : i * m + m]
        print(str)

print_mxn("아이엠어보이유알어걸", 3)

# 228

# def calc_monthly_salary(annual_salary):
#     print(int(annual_salary / 12))

def calc_monthly_salary(annual_pay) :
    monthly_pay = int(annual_pay / 12)
    return monthly_pay

calc_monthly_salary(12000009)

# 229

def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(a=100, b=200) # 왼쪽: 100, 오른쪽: 200

# 230

def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(b=100, a=200) # 왼쪽: 200, 오른쪽: 100