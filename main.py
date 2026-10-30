class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Рахунок поповнено на {amount} грн.")
        else:
            print("Сума поповнення повинна бути більшою за 0.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Сума зняття повинна бути більшою за 0.")
        elif amount <= self.balance:
            self.balance -= amount
            print(f"Знято {amount} грн.")
        else:
            print("Недостатньо коштів на рахунку.")

    def show_balance(self):
        print(f"Номер рахунку: {self.account_number}")
        print(f"Баланс: {self.balance} грн.")


account = BankAccount("123456789", 1000)

account.show_balance()

account.deposit(500)
account.withdraw(300)

account.show_balance()