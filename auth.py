from data import *


class AuthManager:
    def __init__(self):
        self.users = load_users()

    def _reload_users(self):
        self.users = load_users()

    def create_account(self, name, email, password):
        for user in self.users:
            if user.email == email:
                print("\nUser already exists!")
                return None
        new_user = self.users.append(User(name, email, password))
        save_users(self.users)
        print(f"\nAccount for {name} created successfully.")
        return new_user

    def login(self, email, password):
        self._reload_users()
        for user in self.users:
            if user.email == email:
                if user.login(password):
                    print(f"\nWelcome, {user.name}")
                    return user
        print("\nInvalid email or password")
        return None

    def logout(self, user):
        user.logout()
        print("\nYou have logged out.")
