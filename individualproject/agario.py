import turtle
import time
import random
import math
from ball import Ball

turtle.tracer(0)
turtle.hideturtle()

RUNNING=True
SLEEP= 0.05
SCREEN_WIDTH= turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT= turtle.getcanvas().winfo_height()/2

MY_BALL=Ball(0,0,0, 0, 30,'blue')
NUMBER_OF_BALLS=5
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=30
MINIMUM_BALL_DX= -5
MAXIMUM_BALL_DX= 5
MINIMUM_BALL_DY= -5
MAXIMUM_BALL_DY= 5

BALLS= []

for i in range(NUMBER_OF_BALLS):
	
	x=random.randint(round(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS), round(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
	
	dx=random.randint(round(MINIMUM_BALL_DX) , round(MAXIMUM_BALL_DX))
	while(dx==0):
		dx=random.randint(round(MINIMUM_BALL_DX), round(MAXIMUM_BALL_DX))
	
	y=random.randint(round(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS), round(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
	
	dy=random.randint(round(MINIMUM_BALL_DY), round(MAXIMUM_BALL_DY))
	while(dy==0):
		dy=random.randint(round(MINIMUM_BALL_DY), round(MAXIMUM_BALL_DY))	
	
	r=random.randint(round(MINIMUM_BALL_RADIUS) , round(MAXIMUM_BALL_RADIUS))
	
	color=(random.random(), random.random(), random.random())
	print(color)
	
	new_ball=Ball(x,y,dx,dy,r,color)

	BALLS.append(new_ball)


def move_all_balls():
	for ball in BALLS:
		ball.move(round(SCREEN_WIDTH), round(SCREEN_HEIGHT))


def collide(ball_a, ball_b):
	if ball_a==ball_b:
		return False
	distance= math.sqrt(math.pow(ball_a.xcor() - ball_b.xcor(),2) + math.pow(ball_a.ycor() - ball_b.ycor(),2))	
	if (distance+10 <= ball_a.r + ball_b.r):
		return True
	else:
		return False

def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if collide(ball_a, ball_b)==True:
				a_radius = ball_a.r
				b_radius = ball_b.r
				X_COORDINATE=random.randint(round(-SCREEN_WIDTH), round(SCREEN_WIDTH))
				Y_COORDINATE=random.randint(round(-SCREEN_HEIGHT), round(SCREEN_HEIGHT))
				RADIUS=random.randint(round(MINIMUM_BALL_RADIUS), round(MAXIMUM_BALL_RADIUS))
				Color=(random.random(), random.random(), random.random())
				X_AXISSPEED=random.randint(round(MINIMUM_BALL_DX), round(MAXIMUM_BALL_DX))
				Y_AXISSPEED=random.randint(round(MINIMUM_BALL_DY), round(MAXIMUM_BALL_DY))
				while (X_AXISSPEED ==0 and Y_AXISSPEED ==0):
					X_AXISSPEED=random.randint(round(MINIMUM_BALL_DX), round(MAXIMUM_BALL_DX))
					Y_AXISSPEED=random.randint(round(MINIMUM_BALL_DY), round(MAXIMUM_BALL_DY))

				if ball_a.r >= ball_b.r:
					ball_b.r= RADIUS
					ball_b.x= X_COORDINATE
					ball_b.y= Y_COORDINATE
					ball_b.goto(ball_b.x, ball_b.y)
					ball_b.color(Color)
					ball_b.shapesize(ball_b.r/10)
					ball_b.r= ball_a.r+1
					ball_a.shapesize(ball_a.r/10)
				else:
					ball_a.r=RADIUS
					ball_a.x= X_COORDINATE
					ball_a.y= Y_COORDINATE
					ball_a.goto(ball_a.x, ball_a.y)
					ball_a.color(Color)
					ball_a.shapesize(ball_a.r/10)
					ball_b.r= ball_b.r+1
					ball_b.shapesize(ball_b.r/10)


def check_myball_collision():
	for ball in BALLS:
		if collide(MY_BALL, ball) == True:
			if MY_BALL.r < ball.r:
				return False
			else:
				X_COORDINATE=random.randint(round(-SCREEN_WIDTH), round(SCREEN_WIDTH))
				Y_COORDINATE=random.randint(round(-SCREEN_HEIGHT), round(SCREEN_HEIGHT))
				RADIUS=random.randint(round(MINIMUM_BALL_RADIUS), round(MAXIMUM_BALL_RADIUS))
				Color=(random.random(), random.random(), random.random())
				X_AXISSPEED=random.randint(round(MINIMUM_BALL_DX), round(MAXIMUM_BALL_DX))
				Y_AXISSPEED=random.randint(round(MINIMUM_BALL_DY), round(MAXIMUM_BALL_DY))
				ball.r = RADIUS
				ball.x = X_COORDINATE
				ball.y = Y_COORDINATE
				ball.goto(x, y)
				ball.dx = X_AXISSPEED
				ball.dy = Y_AXISSPEED
				ball.color(Color)
				ball.shapesize(ball.r/10)
				MY_BALL.r = MY_BALL.r+1
				MY_BALL.shapesize(MY_BALL.r/10)
	return True

def movearound(event):
	MY_BALL.goto(event.x - round(SCREEN_WIDTH) , round(SCREEN_HEIGHT) - event.y)

turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()


while RUNNING==True:
	if SCREEN_WIDTH != turtle.getcanvas().winfo_width()/2 or SCREEN_HEIGHT != turtle.getcanvas().winfo_height()/2 :
		SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
		SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
	
	move_all_balls()
	check_all_balls_collision()
	RUNNING = check_myball_collision()
	turtle.getscreen().update()
	time.sleep(SLEEP)

turtle.mainloop()
