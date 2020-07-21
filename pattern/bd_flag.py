import turtle

flag=turtle.Turtle()
sc= turtle.Screen()
sc.title("Bangladesh Flag")

sc.bgcolor("black")
flag.pensize(3)
flag.color("grey")

# draw code
# Line
flag.penup()
flag.goto(0,-300)
flag.pendown()
flag.goto(0,200)

# square
flag.begin_fill()
flag.color("#006745")
flag.fillcolor("#006745")

flag.forward(300)
flag.right(90)

flag.forward(200)
flag.right(90)

flag.forward(300)
flag.right(90)

flag.color("grey","#006745")
flag.forward(200)

flag.end_fill()


# Red Circle
flag.penup()
flag.goto(93,100)
flag.pendown()
flag.begin_fill()

flag.fillcolor("#DB2416")
flag.color("#DB2416")
flag.circle(-50)
flag.end_fill()


flag.hideturtle()
turtle.Screen().exitonclick()