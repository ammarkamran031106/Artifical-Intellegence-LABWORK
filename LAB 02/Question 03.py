#You are designing a simple banking system where each customer has a bank account. The
#account balance should be private and not directly accessible from outside the class. Your task
#is to create a BankAccount class with a private attribute __balance and public methods to
#deposit, withdraw, and get_balance. Create a few account objects and use these methods to
#perform transactions, observing how encapsulation protects the balance from direct access.
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance 

    def deposit(self, amount):
        self.__balance = self.__balance + amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance = self.__balance - amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance


# Creating objects
acc1 = BankAccount("Ali", 5000)
acc2 = BankAccount("Sara", 3000)

acc1.deposit(2000)
print("Ali balance:", acc1.get_balance())

acc2.withdraw(1000)
print("Sara balance:", acc2.get_balance())

# print(acc1.__balance)  # ERROR BCZ OF NO ACCESS FOR THIS VAR IN CLASS ITS PRIVATE MEMBER
