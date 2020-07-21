import turtle

graphics = turtle.Turtle()
graphics.color("white")


bg = turtle.Screen()
bg.bgcolor("black")
bg.title("Game")    # add title of the canvas

bg.bgpic("google.gif")  # Support only gif image file formate

# turtle.done()
turtle.Screen().exitonclick()
# bg.exitonclick()
