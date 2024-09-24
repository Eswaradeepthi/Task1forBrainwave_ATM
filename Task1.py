class ATM:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance

    def verify_pin(self):
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.pin:
            return True
        else:
            print("Incorrect PIN. Please try again.")
            return False

    def check_balance(self):
        print(f"Your current balance is: ₹{self.balance}")

    def deposit(self):
        try:
            amount = float(input("Enter the amount to deposit: ₹"))
            if amount > 0:
                self.balance += amount
                print(f"₹{amount} deposited successfully.")
            else:
                print("Deposit amount must be greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

    def withdraw(self):
        try:
            amount = float(input("Enter the amount to withdraw: ₹"))
            if amount > 0:
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"₹{amount} withdrawn successfully.")
                else:
                    print("Insufficient balance.")
            else:
                print("Withdrawal amount must be greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

    def change_pin(self):
        old_pin = input("Enter your current PIN: ")
        if old_pin == self.pin:
            new_pin = input("Enter your new PIN: ")
            confirm_pin = input("Confirm your new PIN: ")
            if new_pin == confirm_pin:
                self.pin = new_pin
                print("PIN changed successfully.")
            else:
                print("PINs do not match. Try again.")
        else:
            print("Incorrect current PIN.")

    def display_menu(self):
        print("\nATM Menu:")
        print("1. Balance Inquiry")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Exit")

    def run(self):
        while True:
            if self.verify_pin():
                while True:
                    self.display_menu()
                    choice = input("Select an option: ")
                    
                    if choice == '1':
                        self.check_balance()
                    elif choice == '2':
                        self.deposit()
                    elif choice == '3':
                        self.withdraw()
                    elif choice == '4':
                        self.change_pin()
                    elif choice == '5':
                        print("Thank you for using the ATM. Goodbye!")
                        return
                    else:
                        print("Invalid option. Please try again.")
            else:
                continue

# Sample usage
if __name__ == "__main__":
    # Initial ATM setup with a default PIN and balance
    atm = ATM(pin="1234", balance=1000)
    atm.run()
