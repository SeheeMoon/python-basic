# 031

a = "3"
b = "4"
print(a+b) # 덧셈 기호는 두 문자열을 연결해준다.

# 032

print("Hi" * 3) # 문자열에 대한 곱셈은 문자열의 반복을 의미한다.

# 033

print("-" * 80)

# 034

t1 = "python"
t2 = "java"

print((t1 + " " + t2 + " ") * 4) # 좀 더 중복을 줄이는 쪽으로 코드를 작성해 보자. ex) 새로운 변수로 지정


# 035

name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13

# print 포맷팅에서 %s는 데이터 타입의 값, %d는 정수형 데이터 타입 값의 출력을 의미한다.

print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))

# 036

print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))

# 037

print(f'이름: {name1} 나이: {age1}')
print(f'이름: {name2} 나이: {age2}') # python f-string

# 038

stock_num = "5,969,782,550"
sn = stock_num.replace(",", "")
sn_int = int(sn)

print(sn_int, type(sn_int))

# 039

quarter = "2020/03(E) (IFRS연결)"

print(quarter[:7])

# 040

data = "    samsung     "
print(data.split()) # strip 메서드를 사용하면 좌우의 공백을 제거할 수 있음.

