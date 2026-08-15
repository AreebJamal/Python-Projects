import turtle

start_x = -200
start_y = 0
no_lines = 8
line_length = 200
angle = 140

turtle.hideturtle()
turtle.speed(0)

# turtle.penup()
# turtle.goto(start_x , start_y)
# turtle.pendown()

for i in range(no_lines):
    turtle.forward(line_length)
    angle = angle+20
    turtle.left(angle)
    angle = angle-10

turtle.done()