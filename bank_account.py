class Bankaccount():
    def __init__(self,balance=0):
        self.balance = balance
    def deposit(self,amount):
        self.balance= self.balance + amount
    def withdraw(self,amount):
        if self.balance<amount:
            print("Insuffiecient Balance")
        else:
            self.balance = self.balance - amount

    def display_balance(self):
        print("Balance:",self.balance)

Bankaccount1= Bankaccount(1000)
Bankaccount1.deposit(200)
Bankaccount1.withdraw(500)
Bankaccount1.display_balance()
bankaccount2 =Bankaccount(500)
bankaccount2.deposit(20)
bankaccount2.withdraw(2000)



