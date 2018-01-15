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
	dx=random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, -SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS)
	while(dx==0):
		dx=random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, -SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS)
	dy=random.randint(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	while(dy==0):
		dy=random.randint(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)	
	MINIMUM_BALL_DX<dx<MAXIMUM_BALL_DX
	MINIMUM_BALL_DY<dy<MAXIMUM_BALL_DY
	MINIMUM_BALL_RADIUS<r<MAXIMUM_BALL_RADIUS
	'color'=random.random()
def new_ball():
	BALLS.append(new_balls)

for move_all_balls in BALLS():










	