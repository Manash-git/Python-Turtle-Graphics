def draw(x,y,color,radius):
    pattern.penup()
    pattern.goto(x,y)
    pattern.pendown()
    pattern.begin_fill()
    pattern.fillcolor(color)
    pattern.circle(radius)
    pattern.end_fill() 
    pattern.penup()   
    pattern.home()

import turtle

pattern = turtle.Turtle()
bg = turtle.Screen()

pattern.pensize(3)


draw(0,-50,"pink",50)
draw(200,200,"green",50)
draw(-200,200,"purple",50)
draw(200,-200,"yellow",-50)
draw(-200,-200,"yellow",-50)

pattern.hideturtle()
turtle.Screen().exitonclick()