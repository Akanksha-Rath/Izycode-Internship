import csv
import random

class BankAccount:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")

    def view_history(self):
        for transaction in self.transaction_history:
            print(transaction)

def read_accounts_from_file(filename):
    accounts = []
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                account = BankAccount(
                    int(row['acc_number']),
                    row['pin'],
                    float(row['balance'])
                )
                accounts.append({'username': row['username'], 'account': account})
    except FileNotFoundError:
        # If the file doesn't exist, return an empty list of accounts
        pass
    return accounts

def write_account_to_file(account, filename):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([account['username'], account['account'].account_number, account['account'].pin, account['account'].balance])

def create_account():
    new_username = input("Enter a unique username: ")
    new_pin = input("Enter your PIN: ")

    existing_accounts = read_accounts_from_file("accounts.csv")

    # Check if the username is unique
    for existing_account in existing_accounts:
        if existing_account['username'] == new_username:
            print("\nUsername already exists. Please choose a different username.")
            return None

    new_account_number = random.randint(1000, 9999)
    new_account = BankAccount(new_account_number, new_pin)
    existing_accounts.append({'username': new_username, 'account': new_account})
    write_account_to_file({'username': new_username, 'account': new_account}, "accounts.csv")
    print(f"\nAccount created successfully!\n\n      WELCOME  {new_username} !!!")

    return new_account

def sign_in():
    username = input("Enter your username: ")
    pin = input("Enter your PIN: ")

    existing_accounts = read_accounts_from_file("accounts.csv")

    for account in existing_accounts:
        if account['username'] == username and account['account'].pin == pin:
            print("Sign-in successful!")
            return account['account']

    print("\nInvalid username or PIN. Sign-in failed.")
    return None

def main():
    authenticated = False
    current_account = None

    while True:
        print("\n1. Create Account")
        print("2. Sign In")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            new_account = create_account()
            if new_account:
                authenticated = True
                current_account = new_account
        elif choice == '2':
            current_account = sign_in()
            authenticated = current_account is not None
        elif choice == '3':
            print("\nExiting program. Have a nice day!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 3.")

        if authenticated:
            # Main menu for authenticated users
            while True:
                print("\n1. Check Balance")
                print("2. Deposit Funds")
                print("3. Withdraw Funds")
                print("4. View Transaction History")
                print("5. Sign Out")

                choice = input("Enter your choice (1-5): ")

                if choice == '1':
                    print(f"\nCurrent Balance: ${current_account.check_balance()}")
                elif choice == '2':
                    amount = float(input("Enter the deposit amount: $"))
                    current_account.deposit(amount)
                    print("\nDeposit successful.")
                elif choice == '3':
                    amount = float(input("Enter the withdrawal amount: $"))
                    current_account.withdraw(amount)
                elif choice == '4':
                    print("\nTransaction History:")
                    current_account.view_history()
                elif choice == '5':
                    print("\nSigning out.")
                    break
                else:
                    print("\nInvalid choice. Please enter a number between 1 and 5.")

# Initialize the CSV file if it doesn't exist
with open("accounts.csv", 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['username', 'acc_number', 'pin', 'balance'])

if __name__ == "__main__":
    main()
