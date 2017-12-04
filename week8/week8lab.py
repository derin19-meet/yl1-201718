from turtle import *
import random
import math
colormode(255)


class Ball(Turtle):
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius)
		self.color(color)
		self.speed(speed)
ball1= Ball(5, 'green', 1)
ball2=Ball(10,'green', 1)

def check_collision(ball1, ball2):
	if (math.sqrt(math.pow(ball1.xcor()-ball2.xcor(),2))+math.pow((ball1.ycor()-ball2.ycor(),2)) 


	ball1.color("yellow")


	
turtle.mainloop()