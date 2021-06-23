class User:		# aqui está lo que tenemos hasta ahora
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account= BankAccount (int_rate = 0.02, balance = 0)
    def make_deposit(self, amount):	# toma un argumento que es el monto del depósito
        self.account.deposit(amount)
        return self

    def make_withdrawal (self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance (self):
        print(f"Usuario: {self.name}, Saldo: {self.account.display_account_info()} ")
        return self
    def transfer_money (self, other_user, amount):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)


class BankAccount:
    def __init__(self, int_rate = 0.02, balance = 0):
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
        
        return self.balance
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.int_rate* self.balance)
        else:
            print("No Hay Saldo!!!")
        return self

gonzalo = User("Gonzalo Ibarra","gonzalo@gmail.com")

gonzalo.make_deposit(100)
gonzalo.make_deposit(300)
gonzalo.make_withdrawal(50)

gonzalo.display_user_balance()
print(gonzalo.account.balance)