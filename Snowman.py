import turtle

def base(rad):
    turtle.circle(rad)
    

def midsec(rad):
    turtle.circle(rad)


def arms():
    turtle.left(30)
    turtle.forward(50)
    turtle.right(15)
    turtle.forward(15)
    turtle.right(180)
    turtle.forward(15)
    turtle.right(100)
    turtle.forward(15)

def head(rad):
    turtle.circle(rad)

    

def hat():
    turtle.right(180)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(10)


if __name__ == '__main__':
    turtle.hideturtle()
    # turtle.goto(0 , -100)
    base(75)
    turtle.penup()
    turtle.goto(0 , 150)
    turtle.pendown()
    midsec(50)
    turtle.penup()
    turtle.goto(50 , 200)
    turtle.pendown()
    arms()
    turtle.penup()
    turtle.goto(-50 , 200)
    turtle.pendown()
    arms()
    turtle.penup()
    turtle.goto(0  , 250)
    turtle.pendown()
    turtle.right(180)
    head(30)
    turtle.penup()
    turtle.goto(-40 , 300)
    turtle.pendown()
    hat()


turtle.done()
