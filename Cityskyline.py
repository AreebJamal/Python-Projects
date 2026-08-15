import turtle

def square(s):
    for i in range(4):
        turtle.forward(s)
        turtle.left(90)

def window(x , y):
    turtle.penup()
    turtle.goto(x+5 ,y-30 )
    turtle.pendown()
    turtle.setheading(0)
    turtle.fillcolor('white')
    turtle.begin_fill()
    square(20)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(x+20 , y-60)
    turtle.pendown()
    turtle.setheading(0)
    turtle.fillcolor('white')
    turtle.begin_fill()
    square(20)
    turtle.end_fill()
    
    
    # turtle.penup()
    # turtle.goto(x+5 , y-30)
    # turtle.goto(x , y)
    # turtle.pendown()


def building():
    lth = 60
    
    turtle.setheading(90)
    turtle.forward(2.5*lth)
    turtle.setheading(0)
    turtle.forward(lth)
    turtle.setheading(90)
    turtle.forward(lth+5)
    turtle.setheading(0)
    turtle.forward(lth+5)
    turtle.setheading(90)
    turtle.forward(3*lth)

    global x
    x = turtle.xcor()
    global y 
    y = turtle.ycor()

    # window(x , y)
    
    # turtle.penup()
    # turtle.goto(x+5 , y-30)
    # turtle.goto(x , y)
    # turtle.pendown()
    turtle.setheading(0)
    turtle.forward(2*lth)
    turtle.setheading(270)
    turtle.forward(3.75*lth)
    turtle.setheading(0)
    turtle.forward(lth)
    turtle.setheading(90)
    turtle.forward(2*lth)

    global a
    a = turtle.xcor()
    global b
    b = turtle.ycor()

    # window(x , y)

    # turtle.penup()
    # turtle.goto(x+5 , y-30)
    # turtle.goto(x , y)
    # turtle.pendown()
    turtle.setheading(0)
    turtle.forward(1.5*lth)
    turtle.setheading(270)
    turtle.forward(lth+5)
    turtle.setheading(0)
    turtle.forward(lth-5)
    turtle.setheading(270)
    turtle.forward(lth+15)
    turtle.setheading(0)
    turtle.forward(lth-10)
    turtle.setheading(270)
    turtle.forward(2.5*lth)
    turtle.setheading(180)
    turtle.forward(500)
     

def stars():
    turtle.pencolor('white')
if __name__ == '__main__':
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-250 , -250)
    turtle.pendown()
    turtle.fillcolor('sky blue')
    turtle.begin_fill()
    square(500)
    turtle.end_fill()
    turtle.fillcolor('misty rose')
    turtle.begin_fill()
    building()
    turtle.end_fill()
    
    window(x ,y)
    window(a ,b)

    turtle.done()

