class Bank_Account:
    def __init__(self):
        self.balance = 0
        print("My balance is 0")
    def withdraw(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("n\ You withdrew:", amount)
        else:
            print("\n Insufficient balance ")
    def deposit(self):
        amount = float(input("Enter amount to be Deopsited: "))
        self.balance += amount
        print("\n Amount Deposited: ", amount)
    def display(self):
        print("\n Net Available Balance=",self.balance)
    
# creating an object of class
s = Bank_Account()
# Calling functions with that class object
s.deposit()
s.withdraw()
s.display()
