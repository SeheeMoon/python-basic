from random import *

class Unit: # 일반 유닛
    def __init__(self, name, hp, speed): # __init__은 파이썬에서 기본적으로 쓰이는 생성자로, 객체를 생성할 때 자동으로 호출되는 부분이다.
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{} 유닛이 생성되었습니다.".format(name))
    
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{} : {} 방향으로 이동합니다. [속도 {}]".format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{} : {} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력은 {} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name)) 



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

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)
    
    # 스팀팩
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))


class Tank(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        
        # 현재 시즈모드가 아닐 때 -> 시즈모드 설정
        if self.seize_mode == False:
            print("{} : 시즈모드로 전환합니다.".format((self.name)))
            self.damage *= 2
            self.seize_mode = True

        # 현재 시즈모드 일 때 -> 시즈모드 해제
        else:
            print("{} : 시즈모드를 해제합니다.".format((self.name)))
            self.damage /= 2
            self.seize_mode = False

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False
 
    def clocking(self):
        if self.clocked == True:
            print("{} : 클로킹 모드를 해제합니다.".format((self.name)))
            self.clocked = False
        else:
            print("{} : 클로킹 모드를 설정합니다.".format((self.name)))
            self.clocked = True

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : gg")
    print("[Player]님이 게임에서 퇴장하셨습니다.")

# 실제 게임 진행

game_start()

# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기 생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 생성
w1 = Wraith()

# 유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.seize_developed = True 
print("[알림]: 탱크 시즈 모드 개발이 완료되었습니다.")

# 공격 모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이스: 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    if isinstance(unit, Tank):
        unit.set_seize_mode()
    if isinstance(unit, Wraith):
        unit.clocking()


# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 20))

# 게임 종료
game_over()



        