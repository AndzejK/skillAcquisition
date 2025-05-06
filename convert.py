# A program to convert Celsius temps to Fahrenheit
# by: Susan Computewell
def main ():
    convertion=eval(input("Enter C if want to covert Celsius temps to Fahrenheit, otherwise type F: "))
    if convertion=='C':
        print("A setting to convert Celsius temps to Fahrenheit.")
        # for i in range(0,110,10): # couted loop
        celsius = eval (input ("What is the Celsius temperature? ") )
            # celsius = i 
        fahrenheit = 9 / 5 * celsius + 32
        print ("The temperature is", fahrenheit, "degrees Fahrenheit.")
            # print(f"{celsius}C -> {fahrenheit}F")
        # input("Press the <Enter> key to quit.") # prevent from closing immediately a cmd window
    else:
        print("A setting to convert Celsius temps to Fahrenheit.")
        fahrenheit = eval (input ("What is the Fahrenheit temperature? ") )
        celsius = 5/9(fahrenheit-32)
        print ("The temperature is", celsius, "degrees Celsius.")
main ()