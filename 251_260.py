# 251

# 클래스는 똑같은 무엇인가를 계속해서 만들어낼 수 있는 설계, 틀과 같은 것이다. 
# 객체는 클래스에 의해서 만들어진 물건, 실체를 뜻한다. 
# 클래스에 의해 만들어진 객체를 인스턴스라고도 한다.
# 객체와 인스턴스의 차이는 클래스와 구체적인 객체 사이의 관계에 초점을 맞추면 인스턴스라는 용어를 사용한다.
# '트럭은 인스턴스'보다는 '트럭은 객체'라는 표현이 어울리고, '트럭은 자동차의 객체'보다는 '트럭은 자동차의 인스턴스'라는 표현이 어울린다.

# 252, 253

# class Human:
#     pass

# areum = Human()

# 254

class Human:
    def __init__(self):
        print("응애응애")

areum = Human()

# 255

class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def __del__(self):
        print("나의 죽음을 알리지 마라")

    def who(self):
        print("이름 : {} 나이 : {} 성별 : {}".format(self.name, self.age, self.sex))
        
    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex



areum = Human("아름", 25, "여자")
print(areum.name)

# 256 

areum = Human("조아름", 25, "여자")
print(areum.age)

# 257
areum.who()

# 258

# areum = Human("불명", "미상", "모름")
# areum.who()      # Human.who(areum)

areum.setInfo("아름", 25, "여자")
areum.who()

# 259

del areum
