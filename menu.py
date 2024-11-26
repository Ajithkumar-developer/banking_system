
class MainMenu:
    def __init__(self, auth_manager, account_manager):
        self.auth_manager = auth_manager
        self.account_manager = account_manager

    def display(self, user):
        while user.is_logged_in:
            print("\nMain Menu")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. View Balance")
            print("4. View Transaction History")
            print("5. Logout")
            print("6. Exit")
            print()

            opt = int(input("Select an option : "))

            if opt == 1:
                amount = float(input("Enter Deposit amount : "))
                self.account_manager.deposit(user, amount)
            elif opt == 2:
                amount = float(input("Enter Withdraw amount : "))
                self.account_manager.withdraw(user,amount)
            elif opt == 3:
                self.account_manager.view_balance(user)
            elif opt == 4:
                self.account_manager.view_transactions_history(user)
            elif opt == 5:
                self.auth_manager.logout(user)
            elif opt == 6:
                print("\nExisting application...")
                break
            else:
                print("\nInvalid choice. Try again!\n")

