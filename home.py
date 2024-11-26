from auth import AuthManager
from account import AccountManager
from menu import MainMenu
def home():
    auth_manager = AuthManager()
    account_manager = AccountManager(auth_manager)

    while True:
        print("\nWelcome to ABC Bank")
        print("--------------------")
        print()
        print("1. Create Account.")
        print("2. Login Account.")
        print("3. Exit.\n")

        opt = int(input("Select an Option : "))

        if opt == 1:
            name = input("Enter your name : ")
            email = input("Enter your Email : ")
            password = input("Enter your password : ")
            auth_manager.create_account(name, email, password)
        elif opt == 2:
            email = input("Enter your email : ")
            password = input("Enter your password : ")
            user = auth_manager.login(email, password)
            if user:
                menu = MainMenu(auth_manager, account_manager)
                menu.display(user)
        elif opt == 3:
            print("\nExisting the application...")
            break
        else:
            print("\nInvalid choice. Try again!\n")