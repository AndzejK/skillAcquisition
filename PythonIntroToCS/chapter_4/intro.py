from graphics import *

win = GraphWin("CS via Python!")

# creation of points/pixels
px1=Point(30,30) # x, y 
px2=Point(198,1)
px3=Point(70,70)
px4=Point(1,198)

# Points for shapes
center = Point(100,100) 

px1_rect=Point(30,30)
px2_rect=Point(70,70)

px1_line=Point(20,30)
px2_line=Point(180,165)

px1_oval=Point(20,150)
px2_oval=Point(180,199)

px1.setFill("green")
px2.setFill("green")
px3.setFill("green")
px4.setFill("green")

#### Shapes ###

# Create a red CIRCLE centered  at (100,100) with radius 30
circle = Circle(center,30)
circle.setFill("red")

# Create a square using a Rectangle object
rect = Rectangle(px1_rect,px2_rect)

# Create a line segment using a Line obj
line = Line(px1_line,px2_line)

# Create an oval using the Oval obj
oval=Oval(px1_oval,px2_oval)

# Labels 
label_center=Text(center,"Red Circle")

while True:
    px1.draw(win) # Draw a created pixel INTO the window
    px2.draw(win) 
    px3.draw(win)
    px4.draw(win)
    circle.draw(win)
    rect.draw(win)
    line.draw(win)
    oval.draw(win)

    label_center.draw(win)
    key = win.getKey()
    if key == 'q':
        print(f"It was pressed {key} bye!")
        break
    


# win.getMouse()