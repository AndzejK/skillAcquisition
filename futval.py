# futval . py
# A program to compute the value of an investment
# carried 10 years into the future
def main () :
    # Intro
    print ("This program calculates the future value")
    print ("of a 10-year investment.")
    
    # Input
    principal = eval (input ("Enter the initial principal: ") )
    apr = eval (input ("Enter the annual interest rate: ") )
    
    # Computation 
    for i in range (10) :
        principal = principal * (1 + apr) # The Distrubutive Property
    
    # Output 
    print ("The value in 10 years is: ", principal)
# main ()

input1,input2 = eval(input("Enter some randon numbers: "))
print(input1,input2)
print(type(input1),type(input2))