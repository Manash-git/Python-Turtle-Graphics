import turtle

text= turtle.Pen()
poly= turtle.Turtle()

# Text code
text.penup()
text.goto(0,-200)
text.write("Polygon Shape ",False, align="center",font=("consolas",15))
text.hideturtle()

# Shape code
for i in range(3,10):
    poly.reset()
    poly.pensize(3)
    poly.circle(100, steps=i)


turtle.Screen().exitonclick()