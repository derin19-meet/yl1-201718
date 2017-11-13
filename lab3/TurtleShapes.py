import turtle
turtle.penup()
turtle.register_shape('square',((-50,0),(0,0),(0,-30),(-30,-60),(-50,-30),(-50,0)))
turtle.shape('square')

turtle.goto(-50,50)
turtle.pendown()
turtle.pencolor('yellow')
turtle.goto(50,50)
turtle.pencolor('red')
turtle.goto(-30,-50)
turtle.pencolor('purple')
turtle.goto(0,100)
turtle.pencolor()
turtle.goto(30,-50)
turtle.pencolor('blue')
turtle.goto(-50,50)

turtle.mainloop()