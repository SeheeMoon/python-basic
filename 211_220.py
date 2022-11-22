# 211

def 함수(문자열) :
    print(문자열)

함수("안녕")
함수("Hi") # "안녕", "Hi"

# 212

def 함수(a, b) :
    print(a + b)

함수(3, 4)
함수(7, 8) # 7, 15

# 213 
# 인자가 전달되지 않았기 때문에 (함수를 호출할 때 하나의 파라미터를 입력해야 한다.)

# 214

# 함수에 연산자가 들어가는데 전달된 파라미터가 문자열과 숫자라 함수의 기능을 수행할 수 없다.

# 215, 216

def print_with_smile(str):
    print(str + ":D")

print_with_smile("안녕하세요")

# 217

def print_upper_price(int):
    print(str(int * 1.3 / 100) + "%")

print_upper_price(10000)

# 218

def print_sum(a, b):
    print(a + b)
print_sum(3, 4)

# 219

def print_arithmetic_operation(a, b):
    print(str(a), "+", str(b), "=", str(a + b))
    print(str(a), "-", str(b), "=", str(a - b))
    print(str(a), "*", str(b), "=", str(a * b))
    print(str(a), "/", str(b), "=", str(a / b))

print_arithmetic_operation(3, 4) # 굳이 str 안 붙여도 됨.

# 220

def print_max(a, b, c):
    if a > b >= c or a > c >= b:
        print(a)
    if b > a >= c or b > c >= a:
        print(b)
    if c > b >= a or c > a >= b:
        print(c)

print_max(300, 40, 30)