from graphics import * 

def main():
    # A default window size 320x240
# main_win=GraphWin("Investment Growth Chart",320,240)

# The value of the investment 10 years into the future.
    principal=float(input("Enter your principal: "))
    apr=float(input("Enter the annual percentage rate: ")) # The annual percentage rate expressed as a decimal number

    for year in range(1,11):
        print(f"Year {year} - {round(principal,2)} $")
        principal=principal*(1+apr)

def draw_one_bar():
    # A default window size 320x240
    main_win=GraphWin("Investment Growth Chart",320,240)
    principal=3000
    apr=.05
    principal=principal*(1+apr)
    print(principal)

# draw_one_bar()