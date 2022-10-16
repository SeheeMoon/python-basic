# 클래스

class Unit: # 일반 유닛
    def __init__(self, name, hp, speed): # __init__은 파이썬에서 기본적으로 쓰이는 생성자로, 객체를 생성할 때 자동으로 호출되는 부분이다.
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{} : {} 방향으로 이동합니다. [속도 {}]".format(self.name, location, self.speed))

# marine = Unit("마린", 40) # 여기서 Unit 클래스를 통해 만들어지는 것들을 객체라고 하며, marine, tank와 같은 것들은 Unit 클래스의 인스턴스라고 한다.
# marine2 = Unit("마린", 40) # __init__함수에서 필요로 하는 인자의 갯수만큼 값을 던져주어야 출력 가능하다.
# tank = Unit("탱크", 150)

# 멤버 변수

# wraith1 = Unit("레이스", 130) # 입력한 "레이스", 130, 10은 각각 name, hp, damage라는 멤버 변수에 할당됨
# wraith2 = Unit("레이스", 130)
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print("생성된 {}는 현재 클로킹 상태입니다.".format(wraith2.name)) # 멤버 변수를 외부에서 활용하는 방법, 멤버 변수를 외부에서 추가해서 다루는 방법 -> 다른 객체에는 적용되지 않음.

# 메소드

class AttackUnit(Unit): # 공격 유닛
    def __init__(self, name, hp, speed, damage): # self는 자기 자신(객체의 인스턴스 그 자체)를 의미. 객체 자기 자신을 참조하는 매개변수이다.
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{} : {} 방향으로 적군을 공격합니다. [공격력 {}]".format(self.name, location, self.damage)) # 함수(메소드)를 호출할 때 self가 붙어있는 name, damage를 제외한 location 값만 넣어서 호출을 해 준다. 

    def damaged(self, damage):
        print("{} : {} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력은 {} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name)) 

# firebat1 = AttackUnit("파이어뱃", 50, 25) 
# firebat1.attack("5시") # 여기서 firebat1은 인스턴스, attack은 메소드가 된다. 메소드와 함수의 차이점은 메소드는 클래스에 종속된 함수이기 때문에 객체와 연결되어 사용된다는 점이다.
# firebat1.damaged(25)
# firebat1.damaged(25)

# 다중 상속
class Flyable: # 날 수 있는 기능을 가진 클래스
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{} : {} 방향으로 날아갑니다. [비행 속도 : {}]".format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable): # 공중 공격 유닛 클래스, 위의 AttackUnit, Flyable 클래스에서 다중상속 받음
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed는 0으로 처리
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location) # 메소드 오버라이딩


valkyrie = FlyableAttackUnit("발키리", 130, 35, 5)
valkyrie.fly(valkyrie.name, "3시")

vulture = AttackUnit("벌쳐", 100, 5, 10)
Battlecruiser = FlyableAttackUnit("배틀크루저", 400, 200, 5)

vulture.move("5시")
Battlecruiser.move("11시")

# pass

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0) # super 함수를 이용하면 마찬가지로 class를 상속받을 수 있는데, 이때 괄호()를 붙어주어야 하고 self는 인자로 받지 않는다.
        self.location = location
        print("[{} 건물이 {} 에 생성되었습니다.]".format(self.name, self.location))

supply_depot = BuildingUnit("서플라이 디폿", 500, "5시")

# def start_game():
#     print("게임을 시작합니다.")

# def game_over():
#     pass

# start_game()
# game_over()

# Quiz 8

class House:
    # 매물 초기화
    def __init__(self,location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type 
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

houses = []
house1 = House("강남", "아파트", "전세", "10억", "2015년")
house2 = House("오이도", "빌라", "매매", "7억", "2005년")
house3 = House("영통", "오피스텔", "월세", "1000/50", "2010년")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {} 대의 매물이 있습니다.".format(len(houses))) # 리스트 안의 자료형의 갯수 셀 때 len을 쓴다.
for house in houses:
    house.show_detail()

# house1.show_detail()
# house2.show_detail()
# house3.show_detail()
