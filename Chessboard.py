import turtle
turtle.hideturtle()
turtle.speed(0)
def darksquare():
    
    turtle.begin_fill()
    for j in range(4):
        turtle.forward(50)
        turtle.left(90)
    turtle.end_fill()

def lightsquare():
    # turtle.forward(50)
    for n in range(4):
        turtle.forward(50)
        turtle.left(90)
    # turtle.forward(50)

turtle.penup()
turtle.goto(-200 , -200)
turtle.pendown()
for i in range(4):
    darksquare()
    turtle.forward(50)
    lightsquare()
    turtle.forward(50)

turtle.left(90)

for i in range(4):
    lightsquare()
    turtle.forward(50)
    darksquare()
    turtle.forward(50)

turtle.left(90)

for i in range(4):
    darksquare()
    turtle.forward(50)
    lightsquare()
    turtle.forward(50)

turtle.left(90)

for i in range(3):
    turtle.forward(50)
    darksquare()
    turtle.forward(50)
    lightsquare()

turtle.forward(50)
turtle.left(90)

for i in range(3):
    turtle.forward(50)
    darksquare()
    turtle.forward(50)
    lightsquare()

turtle.forward(50)
turtle.left(90)

for i in range(3):
    turtle.forward(50)
    darksquare()
    turtle.forward(50)
    lightsquare()

turtle.left(90)
 
for i in range(3):
    darksquare()
    turtle.forward(50)
    lightsquare()
    turtle.forward(50)

turtle.left(90)

for i in range(2):
    turtle.forward(50)
    darksquare()
    turtle.forward(50)
    lightsquare()

turtle.forward(50)
turtle.left(90)

for i in range(2):
    turtle.forward(50)
    darksquare()
    turtle.forward(50)
    lightsquare()

turtle.forward(50)
turtle.left(90)

for i in range(2):
    turtle.forward(50)
    darksquare()
    turtle.forward(50)
    lightsquare()

turtle.left(90)

for i in range(2):
    turtle.forward(50)
    lightsquare()
    turtle.forward(50)
    darksquare()

turtle.left(90)

for i in range(1):
    turtle.forward(50)
    darksquare()
    turtle.forward(50)
    lightsquare()

turtle.forward(50)
turtle.left(90)

for i in range(1):
    turtle.forward(50)
    darksquare()
    turtle.forward(50)
    lightsquare()

turtle.forward(50)
turtle.left(90)

for i in range(1):
    lightsquare()
    turtle.forward(50)
    darksquare()
    turtle.forward(50)


turtle.done()