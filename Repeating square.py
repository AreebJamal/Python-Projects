import turtle

num_square = 100
angle = 90
turtle.hideturtle()
side = 5
x = 200
y= -200
turtle.penup()
turtle.goto(x , y)
turtle.pendown()
turtle.speed(0)

for i in range(num_square):
    for j in range(4):
        turtle.left(angle)
        turtle.forward(side)
        
        
    side = side+5

turtle.done()