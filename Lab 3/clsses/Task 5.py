class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Депозит: {amount}. Баланс теперь: {self.balance}")
        else:
            print("Сумма депозита должна быть положительной.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств на счёте.")
        elif amount > 0:
            self.balance -= amount
            print(f"Снятие: {amount}. Баланс теперь: {self.balance}")
        else:
            print("Сумма снятия должна быть положительной.")

    def __str__(self):
        return f"Владелец: {self.owner}, Баланс: {self.balance}"


account = BankAccount("Иван", 100)
print(account)

account.deposit(50)
account.withdraw(30)
account.withdraw(200)
