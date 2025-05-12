from graphics import *

win = GraphWin("Test113")
while True:
    key = win.getKey()
    if key == 'q':
        print(f"It was pressed {key} bye!")
        break
    else:
        print(key)


# win.getMouse()