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

# my_dict = {"10/26" : [100, 130, 100, 100],
#            "10/27" : [10, 12, 10, 11]}

# def print_value_by_key(dic, key):
#     if 
#     for value in dic.values():
#         print(value)