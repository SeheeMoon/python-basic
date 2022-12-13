# 261

class Stock:
    pass

# 262

class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code

삼성 = Stock("삼성전자", "005930")

print(삼성.name)
print(삼성.code)

# 263

class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def set_name(self,name):
        self.name = name

a = Stock(None, None)
a.set_name("삼성전자")
print(a.name)

# 264

class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def set_name(self,name):
        self.name = name

    def set_code(self, code):
        self.code = code

a = Stock(None, None)
a.set_code("005930")
print(a.code)

# 265

class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def set_name(self,name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name
    
    def get_code(self):
        return self.code

삼성 = Stock("삼성전자", "005930")
print(삼성.name, 삼성.code)

print(삼성.get_name())
print(삼성.get_code())

# 266

class Stock:
    def __init__(self, name, code, PER, PBR, profit):
        self.name = name
        self.code = code
        self.PER = PER
        self.PBR = PBR
        self.profit = profit

    def set_name(self,name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name
    
    def get_code(self):
        return self.code
    
a = Stock("삼성전자", '005930', 15.79, 1.33, 2.83)
print(a.profit)

# 268

class Stock:
    def __init__(self, name, code, PER, PBR, profit):
        self.name = name
        self.code = code
        self.PER = PER
        self.PBR = PBR
        self.profit = profit

    def set_name(self,name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name
    
    def get_code(self):
        return self.code
    
    def set_per(self, PER):
        self.PER = PER
    
    def set_PBR(self, PBR):
        self.PBR = PBR
    
    def set_dividend(self, profit):
        self.profit = profit

# 269

a = Stock("삼성전자", '005930', 15.79, 1.33, 2.83)
a.set_per(12.75)
print(a.PER)

 # 270

삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

lst = [삼성, 현대, LG]
for x in lst:
    print(x.code)
    print(x.PER)