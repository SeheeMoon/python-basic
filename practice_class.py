class Unit:
    def __init__(self):
        print("Unit 생성자")
 
class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__()
        Unit.__init__(self) # 다중상속 받을 시에는, super 함수를 쓰면 마지막에 상속받는 class가 호출되지 않는다는 문제점 발생. 따라서 다중상속 시에는 하나하나 상속, 초기화 해주어야 함.
        Flyable.__init__(self)

dropship = FlyableUnit()

