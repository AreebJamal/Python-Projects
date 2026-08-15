from math import radians
import turtle

#Square
# i=5
# turtle.hideturtle()
# turtle.speed(0)
# while i<410:
#     turtle.left(90)
#     turtle.forward(i)
    
#     i=i+10

# turtle.done()



#Circle
a = 0.1
turtle.speed(0)
turtle.hideturtle()
for j in range(25):

    for i in range(180):
       
        turtle.forward(a)
        turtle.left(1)

    a=a+0.1


turtle.done()
