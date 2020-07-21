import turtle
candy= turtle.Turtle()
bg= turtle.Screen()
bg.bgcolor("black")

color_palet = ["yellow","red","blue","green","white"]
candy.hideturtle()
candy.speed("fastest")
for i in range(300):
    candy.color(color_palet[i%5])
    candy.pensize(i/10+1)
    candy.forward(i+2)
    candy.left(59)

turtle.Screen().exitonclick()