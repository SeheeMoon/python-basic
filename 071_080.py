# 071

my_variable = ()

print(type(my_variable))

# 072

movie_rank = ('닥터 스트레인지', '스플릿', '럭키')
print(movie_rank)

# 073

num1 = (1)
print(num1)

# 074

# 튜플은 안의 내용 변경 불가?! -> 원소의 값 (element)를 변경할 수 없다.

# 075

t = 1, 2, 3, 4
print(type(t))
# 이렇게 괄호 없이 변수를 지정해도 타입은 튜플로 저장된다.

# 076

t = ('a', 'b', 'c')
t = ('A', 'b', 'c')

print(t) # 튜플의 값은 변경할 수 없기 때문에, 새로운 튜플을 만들고 변수를 다시 지정해 주면 된다.

# 077

interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = list(interest)
print(interest)
print(type(interest))

# 078

interest = ['삼성전자', 'LG전자', 'SK Hynix']
interest = tuple(interest)
print(interest)
print(type(interest))

# 079

temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c) # 이를 튜플 언팩킹이라 한다.

# 080

# tuple = ()
# while i in range(1, 100):

data = tuple(range(2, 100, 2))
print(data) #tuple과 range 함수를 이용하여 튜플을 만들 수 있다.
    