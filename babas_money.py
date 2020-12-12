"""
p = principle (present value)
r = interest rate
n = num of compound periods
t = num of years
balance = total @ the end time
earnings = total amount earned
roi = return on investment 

"""
class Bank_Account:
    def __init__(self,balance,name):
        self.balance = balance
        self.name = name
        print("My balance is 0")
    def withdraw(self):
        amount = float(input("Enter amount to be withdrawn: "))

        if self.balance >= amount:
            self.balance -= amount
            print("\n You withdrew:", amount)
        else:
            print("\n Insufficient principle ")

    def display(self):
        print(self.name, ": \t Net Available principle=", self.balance)

    def compound_interest(self, p, r, n ,t):
        p = float(input("What's the principle: $ "))
        r = float(input("What's the rate? % = "))
        n = int(input("how many periods per year: "))
        t = int(input("How many years? "))

        balance = p * (pow((1 + r/100/n), n * t ))
        earnings = balance - p
        roi = earnings / balance * 100 

        print("\n", "You earned $", round (earnings,2), "during the",t,"year period. ")
        print("Balance at the end of the period ",round(balance,2), "\n")
        print("Interest earned is ",round(roi,2), "% returned on investment.")

    def mortgage_payment(self, n, rate):
        p = self.balance * (rate/12/100 * pow((1 + rate/12/100),n))/(pow((1 + rate/12/100),n)-1)

# Driver code

gabe_account = Bank_Account(318200, "gabe")
print(gabe_account.display())
# s.mortgage_payment(360, 2.875)

# s.compound_interest(5000, 10, 12, 5)

andrew_account = Bank_Account(7000000000000, "rich")
print(andrew_account.display())

aris_account = Bank_Account(0, "broke")
print(aris_account.display())

jacore_account = Bank_Account(100000, "jacore")
print(jacore_account.display())





"""
interest = x * balance

12.68 = x * 112.68

12.68/112.68 = x * 112.68/112.68  

x = 0.11255 

x = 100 * 0.12555  

x = 11.255 and/or x = 11.26%

roi = return on investment = 11.26%
"""
