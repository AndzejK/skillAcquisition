def main():
    print("This program illustrates a chaotic funtion")
    x = eval(input("Enter a num between 0 and 1: "))
    for i in range(10):
        x=3.9*x*(1-x)
        print(x)

# main()