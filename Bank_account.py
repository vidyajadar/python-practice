class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance
        self.__transactions = []

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            self.__transactions.append("Deposited Rs{amount}")
            print("Rs{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")
        
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            self.__transactions.append("Withdrawn Rs{amount}") 
            print("Rs {amount} withdrawn successfully.")
        else:
            print("insuffient balance")

    def transfer(self, receiver, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            receiver.__balance += amount

            self.__transactions.append("Transferred {amount} to {receiver.account_holder}")
            receiver.__transactions.append("Received {amount} from {self.account_holder}")

            print("{amount} transfered to {receiver.account_holder}")
        else:
            print("insufficient balance for transfer")

    def check_balance(self):
        print("Current balance: {self.balance}") 

    def transaction_history(self):
        print("transaction history of {self.account_holder}")
        for transaction in self.__transactions:
            print(transaction) 

account1 = BankAccount("Vidya", 10000)
account2 = BankAccount("Ravi", 2000)

account1.deposit(2000)
account1.withdraw(1500)
account1.transfer(account2, 3000)

account1.check_balance()
account2.check_balance()

account1.transaction_history()
account2.transaction_history()