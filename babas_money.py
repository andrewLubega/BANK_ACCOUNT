"""
p = principle (present value)
r = interest rate
n = how many payments per period
t = how many periods
pv = future value

"""
p = float(input("What's the principle: "))
r = float(input("What's the rate: "))
n = int(input("how many periods: "))
t = int(input("How many payments per period: "))
pv = p * (pow((1 + r/100/n),n * t))
          
print (pv)

def compound_interest(p, r, n ,t):
    balance = p * (pow((1 + r/100/n), n * t ))
    ci = balance - p
    print("Balance at the end of the period ",round(balance,2))
    print("Interest earned is ",round(ci,2))

compound_interest(5000, 10, 12, 5)
