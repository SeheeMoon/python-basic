# 201

def print_coin():
    print("비트코인")

# 202

print_coin()

# 203

for i in range(100):
    print_coin()

# 204

def print_coins():
    for i in range(100):
        print_coin()

print_coins()

# 205

# hello()
# def hello():
#     print("Hi") 함수가 정의되기 전에 호출됨.

# 206

def message() :
    print("A")
    print("B")

message()
print("C")
message() #  ABCAB

# 207

print("A")

def message() :
    print("B")

print("C")
message() # ACB

# 208

print("A")
def message1() :
    print("B")
print("C")
def message2() :
    print("D")
message1()
print("E")
message2() # ACBED

# 209

def message1():
    print("A")

def message2():
    print("B")
    message1()

message2() # BA

# 210

def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()

message3() # BCBCBCA