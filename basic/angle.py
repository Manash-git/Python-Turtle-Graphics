import turtle

g= turtle.Turtle()
g.color("white")
g.speed(1)

# movement and direction
g.setheading(90)
g.forward(100)
g.setheading(330)
g.forward(200)
g.setheading(180)
g.backward(200)
g.reset()

bg = turtle.Screen()
bg.bgcolor("black")

turtle.Screen().exitonclick()