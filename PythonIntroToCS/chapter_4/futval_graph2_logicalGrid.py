from graphics import * 

def main():
    # A default window size 320x240
    main_win=GraphWin("Investment Growth Chart",320,240)
    main_win.setCoords(-1,-1,10,10000)
    
    principal=3000
    Rectangle(Point(0,0),Point(1,principal)).draw(main_win).setFill("green") 
    Text(Point(0,principal),principal).draw(main_win).setFill("white")
    apr=.05
    principal=principal*(1+apr)
    principal2=principal*(1+apr)
    print(principal)
    Rectangle(Point(1,0),Point(2,principal)).draw(main_win).setFill("green")
    Rectangle(Point(2,0),Point(3,principal2)).draw(main_win).setFill("green")
    
    Text(Point(1,principal/2),principal).draw(main_win).setFill("white")
    Text(Point(2,principal2/4),principal2).draw(main_win).setFill("white")
    while True:

        key=main_win.getKey()
        if key=='q':
            break

# draw_one_bar()
