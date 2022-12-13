
# 271

from random import *

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        num1 = randrange(0, 1000)
        num2 = randrange(0, 100)
        num3 = randrange(0, 1000000)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account = num1 + "-" + num2 + "-" + num3

kim = Account("김민수", 100)
print(kim.name)
print(kim.balance)
print(kim.bank)
print(kim.account)

# 272

class Account:

    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        num1 = randrange(0, 1000)
        num2 = randrange(0, 100)
        num3 = randrange(0, 1000000)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account = num1 + "-" + num2 + "-" + num3

        Account.account_count += 1
        
kim = Account("김민수", 100)
print(Account.account_count)
lee = Account("이민수", 100)
print(Account.account_count)

# 273

class Account:

    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        num1 = randrange(0, 1000)
        num2 = randrange(0, 100)
        num3 = randrange(0, 1000000)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account = num1 + "-" + num2 + "-" + num3

        Account.account_count += 1

    def get_account_num(cls):
        print(cls.account_count)


kim = Account("김민수", 100)
lee = Account("이민수", 100)
park = Account("박지성", 300)
kim.get_account_num()
lee.get_account_num()

# 274

class Account:

    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        num1 = randrange(0, 1000)
        num2 = randrange(0, 100)
        num3 = randrange(0, 1000000)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account = num1 + "-" + num2 + "-" + num3

        Account.account_count += 1

    def get_account_num(cls):
        print(cls.account_count)

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount
        print("{} current balance : {}".format(self.name, self.balance))

kim = Account("김민수", 300)
kim.deposit(100)


# 275

class Account:

    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        num1 = randrange(0, 1000)
        num2 = randrange(0, 100)
        num3 = randrange(0, 1000000)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account = num1 + "-" + num2 + "-" + num3

        Account.account_count += 1

    def get_account_num(cls):
        print(cls.account_count)

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount
            print("{} current balance : {}".format(self.name, self.balance))
    
    def withdraw(self, amount2):
        if self.balance >= amount2:
            self.balance -= amount2
            print("{} current balance : {}".format(self.name, self.balance))

moon = Account("문세희", 1000)
moon.withdraw(200)

# 276

class Account:

    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        num1 = randrange(0, 1000)
        num2 = randrange(0, 100)
        num3 = randrange(0, 1000000)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account = num1 + "-" + num2 + "-" + num3

        Account.account_count += 1

    def get_account_num(cls):
        print(cls.account_count)

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount
            print("{} current balance : {}".format(self.name, self.balance))
    
    def withdraw(self, amount2):
        if self.balance >= amount2:
            self.balance -= amount2
            print("{} current balance : {}".format(self.name, self.balance))

    def display_info(self):
        print("은행이름: {}".format(self.bank))
        print("예금주: {}".format(self.name))
        print("계좌번호: {}".format(self.account))
        print("잔액: {:,}원".format(self.balance))

Moon = Account("문세희", 1500000000)
Moon.display_info()

# 277

class Account:

    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        num1 = randrange(0, 1000)
        num2 = randrange(0, 100)
        num3 = randrange(0, 1000000)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account = num1 + "-" + num2 + "-" + num3

        Account.account_count += 1

    def get_account_num(cls):
        print(cls.account_count)

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount
            print("{} current balance : {}".format(self.name, self.balance))
    
    def withdraw(self, amount2):
        if self.balance >= amount2:
            self.balance -= amount2
            print("{} current balance : {}".format(self.name, self.balance))

    def display_info(self):
        print("은행이름: {}".format(self.bank))
        print("예금주: {}".format(self.name))
        print("계좌번호: {}".format(self.account))
        print("잔액: {:,}".format(self.balance))

    def interest(self):
        
