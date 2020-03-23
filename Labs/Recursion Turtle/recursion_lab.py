'''
Turtle Recursion (30pts)

1)  Using the turtle library, create the H fractal pattern as shown in the image (htree4.jpg) in this directory. (15pts)

2)  Using the turtle library, create any of the other recursive patterns in the directory. (10pts)

3)  Create your own work of art with a repeating pattern of your making.  It must be a repeated pattern using recursion. Snowflakes, trees, and spirals are a common choice.  Or you can create a third one from the directory. (5pt)


 Each fractal should
 - be recursive
 - have a depth of at least 4
 - be contained on the screen

  Have fun!

'''
import turtle

my_turtle = turtle.Turtle()
my_turtle.showturtle()
my_turtle.shape('turtle')
my_turtle.speed(0)

my_screen = turtle.Screen()
my_screen.bgcolor('white')



def recursive_h(x, y, height, width, depth):
    if depth > 0:
        my_turtle.width(4)
        my_turtle.up()
        my_turtle.goto(x,y)
        my_turtle.down()
        my_turtle.setheading(0)
        my_turtle.forward(width/2)
        my_turtle.left(90)
        my_turtle.forward(height / 2)
        my_turtle.right(180)
        my_turtle.forward(height)
        my_turtle.right(180)
        my_turtle.forward(height/2)
        my_turtle.left(90)
        my_turtle.forward(width)
        my_turtle.right(90)
        my_turtle.forward(height / 2)
        my_turtle.left(180)
        my_turtle.forward(height)
        recursive_h(x - width / 2, y + height / 2, height / 2, width / 2, depth - 1)
        recursive_h(x - width / 2, y - height / 2, height / 2, width / 2, depth - 1)
        recursive_h(x + width / 2, y - height / 2, height / 2, width / 2, depth - 1)
        recursive_h(x + width / 2, y + height / 2, height / 2, width / 2, depth - 1)

def recursive_h(x, y, height, width, depth):
    if depth > 0:
        my_turtle.width(4)
        my_turtle.up()
        my_turtle.goto(x,y)
        my_turtle.down()
        my_turtle.setheading(0)
        my_turtle.forward(width/2)
        my_turtle.left(90)
        my_turtle.forward(height / 2)
        my_turtle.right(180)
        my_turtle.forward(height)
        my_turtle.right(180)
        my_turtle.forward(height/2)
        my_turtle.left(90)
        my_turtle.forward(width)
        my_turtle.right(90)
        my_turtle.forward(height / 2)
        my_turtle.left(180)
        my_turtle.forward(height)
        recursive_h(x - width / 2, y + height / 2, height / 2, width / 2, depth - 1)
        recursive_h(x - width / 2, y - height / 2, height / 2, width / 2, depth - 1)
        recursive_h(x + width / 2, y - height / 2, height / 2, width / 2, depth - 1)
        recursive_h(x + width / 2, y + height / 2, height / 2, width / 2, depth - 1)


recursive_h(0,0,300, 300, 4)

my_screen.exitonclick()







import matplotlib.pyplot as ply
import random
plt.plot([1, 2, 3, 4])