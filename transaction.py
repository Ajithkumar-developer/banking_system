class Transaction:
    def __init__(self, date, user_email, transaction_type, amount, resulting_balance):
        self.date = date
        self.user_email = user_email
        self.transaction_type = transaction_type
        self.amount = amount
        self.resulting_balance = resulting_balance

    def display(self):
        return f"{self.date}  |  {self.user_email}  |  {self.transaction_type}  |  {self.amount}  |  New Balance : {self.resulting_balance}"
