from graphics import * 

# A default window size 200x200
main_win=GraphWin("Tic-Tac-Toe",500,500)

# set coordinates 
main_win.setCoords(0,0,3,3)

# Draw vertical lines, Y, |
p1_x_y = Point(1,0)
p2_x_y = Point(1,3)
p3_x_y = Point(2,0)
p4_x_y = Point(2,3)

Line(p1_x_y,p2_x_y).draw(main_win)
Line(p3_x_y,p4_x_y).draw(main_win)


## Line N01
ph1_x_y = Point(0,1)
ph2_x_y = Point(3,1)

## Line N02
ph3_x_y = Point(0,2)
ph4_x_y = Point(3,2)

# Draw horizontal Line(s), X, ----
Line(ph1_x_y,ph2_x_y).draw(main_win)
Line(ph3_x_y,ph4_x_y).draw(main_win)


key = main_win.getKey()
while True:
    
    if key == 'q':
        break
