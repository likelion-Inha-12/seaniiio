class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    # 1. 입금
    def deposit(self, money):
        if money < 0:
            print("금액은 양수여야 합니다.")
        else:
            print("%s원이 입금되었습니다" % money)
            self.balance += money

    # 2. 출금
    def withdrawal(self, money):
        if money < 0:
            print("금액은 양수여야 합니다.")
        elif self.balance > money:
            print("%s원이 출금되었습니다" % money)
            self.balance -= money
        else:
            print("출금 금액이 잔액을 초과하거나 잘못 입력되었습니다.")
    
    # 3. 잔액 확인
    def get_balance(self):
        print("%s님의 계좌 잔액은 %d원입니다." % (self.name, self.balance))


# acc1 = Account("김시원", 1000)
# acc1.get_balance()
# acc1.deposit(500)
# acc1.withdrawal(200)
# acc1.get_balance()

# acc2 = Account("김시원", 1000)
# acc2.get_balance()
# acc2.deposit(500)
# acc2.withdrawal(2000)
# acc2.get_balance()

# acc3 = Account("김시원", 1000)
# acc3.get_balance()
# acc3.withdrawal(-500)
# acc3.withdrawal(2000)
# acc3.get_balance()