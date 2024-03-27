from 실습2 import Account

class SavingAccount(Account):
    def __init__(self, name, balance, interest_rate):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def deposit(self, money):
        # 1. 초기 잔액 표시
        print("%s님의 계좌 잔액은 %s원입니다." % (self.name, self.balance))
        print("이자율: %s%%" % (self.interest_rate * 100))
        super().deposit(money)

    # 2. 이자 추가하기
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print("%s님의 계좌에 %.1f원의 이자가 추가되었습니다." % (self.name, interest))
    
    # 3. 최종 잔액 표시
    def get_final_balance(self):
        print("%s님의 계좌 잔액은 %.1f원입니다." % (self.name, self.balance))
        print("이자율: %s%%" % (self.interest_rate * 100))

acc1 = SavingAccount("김시원", 1000, 0.05)
acc1.deposit(500)
acc1.add_interest()
acc1.withdrawal(100)
acc1.get_final_balance()