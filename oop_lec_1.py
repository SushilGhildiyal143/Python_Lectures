class Atm():
    def __init__(self):
        self.pin = ""
        self.balance = 0    

        self.menu()
    
    def menu(self):
        user_input = input("""
        Welcome to the ATM
        Please choose an option:
        1. Enter 1 to Create Pin
        2. Enter 2 to Deposit
        3. Enter 3 to Withdraw
        4. Enter 4 to Check Balance
        5. Enter 5 to Exit

        """)
        if user_input == "1":
            # print("Create Pin")
            self.create_pin()
        elif user_input == "2":
            # print("Deposit")
            self.deposit()
        elif user_input == "3":
            # print("Withdraw")
            self.withdraw()
        elif user_input == "4":
            # print("Check Balance")
            self.check_balance()
        else:
            print("Exit")

    def create_pin(self):
        self.pin = int(input("Please enter your new pin: "))
        print("Pin created successfully")

    def deposit(self):
        temp = int(input("Please enter your pin: "))
        if temp == self.pin:
            amount = float(input("Please enter the amount to deposit: "))
            self.balance += amount
            print("Deposit successful. Your new balance is: ", self.balance)
        else:
            print("Invalid pin. Please try again.")

    def withdraw(self):
        temp = int(input("Please enter your pin: "))
        if temp == self.pin:
            amount = float(input("Please enter the amount to withdraw: "))
            if amount <= self.balance:
                self.balance -= amount
                print("Withdrawal successful. Your new balance is: ", self.balance)
            else:
                print("Insufficient funds. Your current balance is: ", self.balance)
        else:
            print("Invalid pin. Please try again.")

    def check_balance(self):
        temp = int(input("Please enter your pin: "))
        if temp == self.pin:
            print("Your current balance is: ", self.balance)
        else:
            print("Invalid pin. Please try again.") 