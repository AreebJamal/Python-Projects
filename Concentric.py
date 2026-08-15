import turtle
#taking information
no_circle = int(input("How many concentric circles you want to create:  "))
start_radius = int(input("Starting radius is:  "))
dis = int(input("Distance b/w concentric circle is:  "))

#setup turtle
turtle.speed(3)
turtle.hideturtle()

#seting radius og first circle
radius = start_radius

#draw the circles
for i in range(no_circle):
    turtle.circle(radius)

    #geting coordinates of next circle(
    x = turtle.xcor()
    y = turtle.ycor() - dis 

    #radius of next circle
    radius = radius + dis

    #position the turtle for next circle
    turtle.penup()
    turtle.goto(x , y)
    turtle.pendown()

turtle.done()