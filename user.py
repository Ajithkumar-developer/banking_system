
class User:
    def __init__(self, name, email, password, balance=0):
        self.name = name
        self.email = email
        self.password = password
        self.balance = balance
        self.is_logged_in = False

    def login(self, password):
        if self.password == password:
            self.is_logged_in = True
            return True
        return False

    def logout(self):
        self.is_logged_in = False

    def update_balance(self, new_balance):
        self.balance = new_balance
