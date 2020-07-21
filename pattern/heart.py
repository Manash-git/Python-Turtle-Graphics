import turtle

love= turtle.Turtle()
sc= turtle.Screen()

sc.title("Hearth Shape")

sc.bgcolor("black")
love.color("pink")

love.pensize(3)
love.left(140)
love.forward(150)
love.circle(-90,180)
love.setheading(39)
love.circle(-90,180)
love.forward(141)

turtle.Screen().exitonclick()