import turtle
draw=turtle.Turtle()

color_pallet = ["yellow","purple","cyan","pink"]

draw.penup()
draw.goto(200,0)
draw.pensize(4)

for i in range(4):
    draw.pendown()
    draw.begin_fill()
    draw.fillcolor(color_pallet[i])
    draw.circle(100)
    draw.end_fill()
    draw.penup()
    draw.backward(100)
    
turtle.Screen().exitonclick()