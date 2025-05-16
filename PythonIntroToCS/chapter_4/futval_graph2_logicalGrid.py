from graphics import * 

def main():
    
    # Introduction
    print("This program plots the growth of a 10-year investment.")
    
    # Get principal and interest rate
    principal = float(input("Enter the init ial principal: "))
    apr = float(input("Enter the annualized interest rate: "))

    # Create a graphics window size of 320x240, 640x480
    main_win=GraphWin("Investment Growth Chart",640,480)
    main_win.setCoords(-1.75,-250,11.5,10500)
    
    
    # Create labels on left edge
    label_0=Text(Point(-1,0),"0.0k")
    label_0.draw(main_win)
    label_1=Text(Point(-1,2500),"2.5k")
    label_1.draw(main_win)
    label_2=Text(Point(-1,5000),"5.0k")
    label_2.draw(main_win)
    label_3=Text(Point(-1,7500),"7.5k")
    label_3.draw(main_win)
    label_4=Text(Point(-1,10000),"10.0k")
    label_4.draw(main_win)

    # Draw bar for initial principal 
    init_bar=Rectangle(Point(0,0),Point(1,principal))
    init_bar.setFill("blue")
    init_bar.setWidth(2) # outline of rectabgle's shape
    init_bar.draw(main_win)

    # Draw a bar f or each subsequent year
    for year in range(1,11):
        principal=principal*(1+apr)

        bar=Rectangle(Point(year,0),Point(year+1,principal))
        bar.setWidth(2)
        bar.setFill("green")
        bar.draw(main_win)

    input("Press any key to quit.")
    main_win.close()

    # while True:

    #     key=main_win.getKey()
    #     if key=='q':
    #         break

main()
