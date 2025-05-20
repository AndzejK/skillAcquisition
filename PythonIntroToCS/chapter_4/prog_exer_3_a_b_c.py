from graphics import *

def main () :
    win = GraphWin( )
    # Draw Rectangle
    shape=Rectangle(Point(50,50),Point(70,70))
    # shape = Circle (Point (50 , 50) , 20)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(3):
        p = win.getMouse()
        c = shape.getCenter()
        print(c)
        print(p)
        dx = p.getX()-c.getX()
        dy = p.getY()-c.getY()
        # shape.move(dx,dy)
        new_shape=shape.clone()
        new_shape.move(dx,dy)
        new_shape.draw(win)
    
    msg=Text(Point(70,25),"Click again to quit")
    msg.draw(win)
    win.getMouse()
    win.close()
main()



def claude_main():
    win = GraphWin("Click for Rectangles", 300, 300)
    
    # Draw original Rectangle
    shape = Rectangle(Point(50, 50), Point(70, 70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    
    # Width and height of the original rectangle (to maintain the same size)
    width = 70 - 50  # 20
    height = 70 - 50  # 20
    
    for i in range(10):
        p = win.getMouse()  # Get click point
        
        # Calculate new rectangle's corner points based on where user clicked
        # We want the CENTER of the new rectangle to be at the clicked point
        p1 = Point(p.getX() - width/2, p.getY() - height/2)  # Top-left corner
        p2 = Point(p.getX() + width/2, p.getY() + height/2)  # Bottom-right corner
        
        # Create and draw the new rectangle
        next_shape = Rectangle(p1, p2)
        next_shape.setOutline("red")
        next_shape.setFill("red")
        next_shape.draw(win)
    
    # Wait for one more click to close the window
    win.getMouse()
    win.close()