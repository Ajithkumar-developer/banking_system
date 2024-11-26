from datetime import datetime

from data import *
class AccountManager:
    def __init__(self, auth_manager):
        self.auth_manager = auth_manager
        self.transactions = load_transactions()

    def _reload_transactions(self):
        self.transactions = load_transactions()

    def view_balance(self, user):
        print(f"\nCurrent balance : {user.balance}")

    def deposit(self, user, amount):
        if amount <= 0:
            print("\nDeposit amount must be positive. ")
            return
        user.balance += amount
        save_users(self.auth_manager.users)
        x = datetime.now()
        time = x.strftime("%d-%m-%Y %I:%M:%S %p")
        transaction = Transaction(time,user.email,"Deposit ",amount,user.balance)
        save_transaction(transaction)
        self._reload_transactions()
        print(f"\nDeposited amount : {amount}  |  New Balance : {user.balance}")

    def withdraw(self, user, amount):
        if amount <= 0:
            print("\nWithdraw amount must be positive. ")
            return
        if amount > user.balance:
            print("\nInsufficient balance!")
            return
        user.balance -= amount
        save_users(self.auth_manager.users)
        x = datetime.now()
        time = x.strftime("%d-%m-%Y %I:%M:%S %p")
        transaction = Transaction(time, user.email, "Withdraw", amount, user.balance)
        save_transaction(transaction)
        self._reload_transactions()
        print(f"\nWithdraw amount : {amount}  |  New Balance : {user.balance}")

    def view_transactions_history(self, user):
        print("\nTransaction History\n")
        self._reload_transactions()
        for transaction in self.transactions:
            if transaction.user_email == user.email:
                print(transaction.display())
        print(f"\nClosing Balance : {user.balance}")
