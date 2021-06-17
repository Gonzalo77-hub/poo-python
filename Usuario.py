class User:		# aqui está lo que tenemos hasta ahora
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # agrega el método deposit 
    def make_deposit(self, amount):	# toma un argumento que es el monto del depósito
        self.account_balance += amount
        return self

    def make_withdrawal (self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance (self):
        print(f"Usuario: {self.name}, Saldo: {self.account_balance} ")
        return self
    def transfer_money (self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        



guido = User("Guido van Rossum","guido@codingdojo.com")
monty = User("Monty Python", "monty@python.com")
gonzalo = User("Gonzalo Ibarra", "gonzalo@gmail.com")

guido.make_deposit(150) .make_deposit(40) .make_deposit(10) .make_withdrawal(20) .display_user_balance()


monty.make_deposit(100) .make_deposit(30) .make_withdrawal(20) .make_withdrawal(20) .display_user_balance()


gonzalo.make_deposit(100000) .make_withdrawal(100) .make_withdrawal(200) .make_withdrawal(400) .display_user_balance()


guido.transfer_money(monty, 20)
guido.display_user_balance()
monty.display_user_balance()

""" guido.display_user_balance()
guido.make_withdrawal(20)
guido.display_user_balance()
guido.transfer_money(monty, 20)
guido.display_user_balance()
monty.display_user_balance()   """  

