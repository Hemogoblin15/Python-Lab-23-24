class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance is ${self.balance}")

    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self.balance}")
        else:
            print("Insufficient funds")


class SavingsAccount(Account):
    def calculate_interest(self, interest_rate):
        interest = self.balance * (interest_rate / 100)
        self.deposit(interest)
        print(f"Interest of ${interest} added. New balance is ${self.balance}")


class CheckingAccount(Account):
    def check_balance(self):
        print(f"Balance is ${self.balance}")

account = Account(123, 450)
account.deposit(50)
account.withdrawal(50)

savingsAccount = SavingsAccount(1234, 300)
savingsAccount.calculate_interest(5)

checkingAccount = CheckingAccount(12345, 400)
checkingAccount.check_balance()