class account():
    def __init__(self,accNo,balance):
        self.balance = balance
        self.accNo = accNo
    
    def debit(self,NEWamount):
        self.balance += NEWamount
        print(NEWamount,"is added debited.")
        print("Total amount = ",self.acc_balance())
    
    def credit(self,NEWamount):
        self.balance -= NEWamount
        print(NEWamount,"is added credited.")
        print("Total amount = ",self.acc_balance())

    def acc_balance(self):
        return self.balance


a1 = account(12345678,10000)

a1.credit(5000)
a1.debit(15000)