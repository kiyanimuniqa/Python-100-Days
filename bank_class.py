class bankaccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def deposit_amount(self,amount):
        self.balance= self.balance + amount
        print(self.balance)
    def withdraw_anount(self,amount):
        if amount > self.balance:
            print("Sorry ! you have not enough balance")
        else:
           self.balance =self.balance - amount
           print(self.balance)
        

        
a =bankaccount("Muniqa",1200)
a.deposit_amount(300)
a.withdraw_anount(4000)
