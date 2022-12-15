# 281

class Car:

    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price

car = Car(2, 1000)
print(car.wheel)
print(car.price)

# 282

class Bicycle(Car):

    def __init__(self):
        pass

# 283

class Bicycle(Car):

    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price


bicycle = Bicycle(2,100)
print(bicycle.price)

# 284

class Bicycle(Car):

    def __init__(self, wheel, price, gear):
        self.wheel = wheel
        self.price = price
        self.gear = gear

bicycle = Bicycle(2,100, "시마노")
print(bicycle.gear)

# 285

class Automobile(Car):

    def __init__(self, wheel, price):
        # self.wheel = wheel
        # self.price = price
        super().__init__(wheel, price)
    
    def info(self):
        print("바퀴수 {}".format(self.wheel))
        print("가격 {}".format(self.price))

car = Automobile(4, 1000)
car.info()

# 286

class Car:

    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price

    def info(self):
        print("바퀴수 {}".format(self.wheel))
        print("가격 {}".format(self.price))

class Bicycle(Car):

    def __init__(self, wheel, price, gear):
        super().__init__(wheel, price)
        self.gear = gear

bicycle = Bicycle(2, 100, "시마노")
bicycle.info()

# 287

class Car:

    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price

    def info(self):
        print("바퀴수 {}".format(self.wheel))
        print("가격 {}".format(self.price))

class Bicycle(Car):

    def __init__(self, wheel, price, gear):
        super().__init__(wheel, price)
        self.gear = gear

    def info(self):
        # print("바퀴수 {}".format(self.wheel))
        # print("가격 {}".format(self.price))
        super().info() # 메소드 오버라이딩
        print("구동계 {}".format(self.gear))

bicycle = Bicycle(2, 100, "시마노")
bicycle.info()

# 288

class 부모:
    def 호출(self):
        print("부모호출")

class 자식(부모):
    def 호출(self):
        print("자식호출")


나 = 자식()
나.호출() # 자식호출이 출력된다.

# 289

class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")

나 = 자식() # 자식생성이 출력된다.

# 290

class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")
    super().__init__()

나 = 자식() # 자식생성, 부모생성이 출력된다.
