import turtle

no_circle = 90
radius = 100
angle = 4
turtle.bgcolor('black')
turtle.pencolor('white')
turtle.pensize(2)
turtle.speed(0)
#draw 36 circles by tilting turtle 10 degrees after each circle
for i in range(no_circle):
    turtle.circle(radius)
    turtle.left(angle)

turtle.done()