# 예외처리

try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(nums[0] / nums[1]))
    print("{} / {} = {}".format(nums[0], nums[1], nums[2]))

except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)

# 에러 발생시키기, 사용자 정의 에러처리

class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 전용 나누기 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("잘못된 값을 입력하였습니다. 한 자리 숫자를 입력해 주세요. 입력값 : {}, {}".format(num1, num2))
    print("{} / {} = {}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자를 입력하세요.")
except BigNumberError as err:
    print(err)

# finally

finally:
    print("계산기를 이용해 주셔서 감사합니다.")


# # Quiz 9

# # 조건 1 : 1보다 작거나 숫자가 아닌 값 입력 시 ValueError로 처리
# #        출력 메시지 : 잘못된 값을 입력하였습니다.
# # 조건 2 : 대기 손님이 주문할 수 있는 치킨 양은 총 10마리로 한정
# #          치킨 소진 시 사용자 정의 에러 [SoldOutError]를 발생시키고 프로그램 종료
# #         출력 메시지 : 재고가 소진되어 더 이상 주문을 받지 않습니다.

chicken = 10
waiting  = 1 # 홀 안에는 만석, 대기번호 1부터 시작

while(True):
    class SoldOutError(Exception):
        def __init__(self, msg):
            self.msg = msg

        def __str__(self):
            return self.msg
    try:
        if chicken == 0:
            raise SoldOutError("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        print("[남은 치킨 : {}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order < 1:
            raise ValueError
        elif order > chicken:
            print("재료가 부족합니다.")
        else:
            print("[대기번호 {}] : {} 마리 주문이 완료되었습니다.".format(waiting, order))
            waiting += 1
            chicken -= order

    except ValueError:
        print("잘못된 값을 입력하였습니다.")

    except SoldOutError as err:
        print(err)
        break

# 모듈
import theater_price as mv

mv.price(3)
mv.morning_price(4)
mv.soldier_price(5)

from theater_price import *
price(3)

# from theater_price import price, morning_price
# price(3)
# morning_price(4)
# soldier_price(3)

from theater_price import soldier_price as price
price(3)







