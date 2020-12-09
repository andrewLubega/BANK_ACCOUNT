"""
p = principle (present value)
r = interest rate
n = num of compound periods
t = num of years
balance = total @ the end time
earnings = total amount earned
roi = return on investment 

"""


def compound_interest(p, r, n ,t):
    p = float(input("What's the principle: $ "))
    r = float(input("What's the rate? % = "))
    n = int(input("how many periods per year/ : "))
    t = int(input("How many years? "))

    balance = p * (pow((1 + r/100/n), n * t ))
    earnings = balance - p
    roi = earnings / balance * 100 

    print("\n", "You earned $", round (earnings, 2), "during the",t,"year period. ")
    print("Balance at the end of the period ",round(balance,2), "\n")
    print("Interest earned is ",round(roi,2), "% returned on investment.")

compound_interest(5000, 10, 12, 5)

"""
interest = x * balance

12.68 = x * 112.68

12.68/112.68 = x * 112.68/112.68  

x = 0.11255 

x = 100 * 0.12555  

x = 11.255 and/or x = 11.26%

roi = return on investment = 11.26%
"""
