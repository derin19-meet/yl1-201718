import turtle
import time
import random
from ball.py import Ball

turtle.tracer(0,1)
turtle.hideturtle()

RUNNING==True
SLEEP= 0.0077
SCREEN_WIDTH= turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT= turtle.getcanvas().winfo_height()/2

MY_BALL=Ball(0,0,100, 500, 10/10,'blue')
NUMBER_OF_BALLS=5
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=100
MINIMUM_BALL_DX= -5
MAXIMUM_BALL_DX= 5
MINIMUM_BALL_DY= -5
MAXIMUM_BALL_DY= 5

BALLS= []

for i in range(NUMBER_OF_BALLS):
	
	x=random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, -SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS)
	
	dx=random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
	while(dx==0):
		x=random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, -SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS)
	
	y=random.randint(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	
	dy=random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
	while(dy==0):
		y=random.randint(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)	
	
	r=random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS) 
	
	color=random.random()
	Ball(0,0,100, 500, 10/10,'blue')

BALLS.append(Ball)

for move_all_balls in BALLS(screen_width, screen_height):
	move(500,500)

def collide(ball_a, ball_b):
	if ball_a==ball_b:
		return False
	calculate.distance(ball_a.r , ball_b.r):
		distance= math.sqrt(math.pow((ball_a.r.MAXIMUM_BALL_RADIUS - ball_a.r.MINIMUM_BALL_RADIUS),2) + math.pow((ball_b.r.MAXIMUM_BALL_RADIUS - ball_b.r.MINIMUM_BALL_RADIUS),2))	
	if Ddistance+10 <= (ball_a.r+ball_b.r):
		return True
	else:
		return False

def check_all_balls_collision():
	for ball_a in BALLS:
	for ball_b in BALLS:
	if collide(ball_a, ball_b)==True:
		a_radius = ball_a.r()
		b_radius = ball_b.r()
	X_coordinate=random.randint(round(-SCREEN_WIDTH), round(SCREEN_WIDTH))
	Y_coordinate=random.randint(round(-SCREEN_HEIGHT, round(SCREEN_HEIGHT))
	dx=random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	dy=random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
	r=random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	



