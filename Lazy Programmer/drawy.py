from turtle import *

speed('fastest')

# Rotate the pen upward to draw the tree 
rt(-90)

# The angle between two branches of Y
angle = 30
colormode(255)
Screen().bgcolor(255, 229, 242)

# Draw Y with a specified size and the depth of the level 
def draw_y(size, level):

    if level > 0:
        colormode(255)
        pencolor(0, 255//level, 0)
        
        # draw the verticle base
        fd(size)

        # draw the right branch
        rt(angle)
        draw_y(0.8 * size, level-1)

        pencolor(0, 255//level, 0)
        # draw the left branch 
        lt( 2 * angle )
        draw_y(0.8 * size, level-1)

        pencolor(0, 255//level, 0)
        # back to the root
        rt(angle)
        fd(-size)
		
		
goto(-250, 0)
draw_y(30, 7)
goto (-100, 0) 
draw_y(50, 7)
goto (150, 0)
draw_y(80, 7)

# Pause to show the image. Enter any key to end the program
x = input()

