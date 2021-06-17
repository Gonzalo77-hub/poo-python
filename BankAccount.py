class BankAccount:
    def __init__(self, int_rate = 0, balance = 0):
        self.int_rate =  int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance < amount:
            print(f"Fondos Insuficientes!!!: Cobrar una tarifa de {amount- self.balance}$")
        else:
            self.balance -= amount
        return self
    def display_account_info(self):
        print(f" Saldo: {self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.int_rate* self.balance)
        else:
            print("No Hay Saldo!!!")
        return self

gonzalo = BankAccount(0.01)
juanito = BankAccount(0.03)

gonzalo.deposit(200).deposit(1000).deposit(500).withdraw(1200).yield_interest().display_account_info()
juanito.deposit(100).deposit(500).withdraw(100).withdraw(200).withdraw(50).withdraw(150).yield_interest().display_account_info