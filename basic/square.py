import turtle
sqr= turtle.Turtle()
sqr.color("white")

bg= turtle.Screen()
bg.bgcolor("black")

sqr.begin_fill()
sqr.fillcolor("pink")

# Square code
for i in range(4):
    sqr.left(90)
    sqr.forward(200)

sqr.end_fill()

sqr.hideturtle()

turtle.Screen().exitonclick()