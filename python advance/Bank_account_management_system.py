class BankAccount:
    total_accounts_created = 0
    bank_name = "SBI"

    def __init__(self, account_holder_name, balance):
        self.account_holder_name = account_holder_name
        self.balance = balance
        self.transaction_history = []  # Keep this as an instance attribute, not a class attribute.
        BankAccount.total_accounts_created += 1  # Update the shared counter on the class.

    def deposit(self, amount):
        if not self.is_valid_amount(amount):
            print("Deposit amount must be positive.")
            return

        self.balance += amount
        self.transaction_history.append(f"Deposited {amount}")
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if not self.is_valid_amount(amount):
            print("Withdraw amount must be positive.")
            return

        if amount > self.balance:
            print("Cannot withdraw: insufficient balance.")
            return

        self.balance -= amount
        self.transaction_history.append(f"Withdrew {amount}")
        print(f"Withdrew {amount}. New balance: {self.balance}")

    @classmethod
    def from_string(cls, data_string):
        account_holder_name, balance = data_string.split("-")
        return cls(account_holder_name, int(balance))

    @staticmethod
    def is_valid_amount(amount):
        return amount > 0


if __name__ == "__main__":
    account1 = BankAccount("Rahul", 1000)
    account2 = BankAccount("Rahul", 1000)

    print("account1 == account2:", account1 == account2)  # Default object comparison, so this is False.
    print("account1 is account2:", account1 is account2)  # Different objects in memory, so this is also False.

    print("Bank name:", BankAccount.bank_name)
    print("Total accounts created:", BankAccount.total_accounts_created)

    account1.deposit(500)
    account1.withdraw(200)
    account1.withdraw(5000)

    account3 = BankAccount.from_string("Ashutosh-5000")
    print("Created from string:", account3.account_holder_name, account3.balance)

    deposit_ref = account1.deposit
    print(deposit_ref)
    deposit_ref(500)

    print("Transaction history:", account1.transaction_history)
