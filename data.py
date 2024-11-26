import os.path
from user import User
from transaction import Transaction

def save_users(users):
    with open("user.txt","w") as file:
        for user in users:
            file.write(f"{user.name},{user.email},{user.password},{user.balance}\n")


def load_users():
    users = []
    if os.path.exists("user.txt"):
        with open("user.txt","r") as file:
            lines = file.readlines()
            for line in lines:
                name, email, password, balance = line.strip().split(',')
                users.append(User(name, email, password, float(balance)))
    return users


def load_transactions():
    transactions = []
    if os.path.exists("transactions.txt"):
        with open("transactions.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                date, user_email, transaction_type, amount, balance = line.strip().split(',')
                transactions.append(Transaction(date, user_email, transaction_type, float(amount), float(balance)))
    return transactions


def save_transaction(transaction):
    with open("transactions.txt","a") as file:
        file.write(f"{transaction.date},{transaction.user_email},{transaction.transaction_type},{transaction.amount},{transaction.resulting_balance}\n")
