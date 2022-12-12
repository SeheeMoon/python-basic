class Moon:
    def __init__(self, who, how, what):
        self.who = who
        self.how = how
        self.what = what
    
    def luv(self):
        print(f"{self.who}는 한률을 {self.how} {self.what}한다.")
    

reply = Moon("문세희", "세상에서 제일", "사랑")
reply.luv()