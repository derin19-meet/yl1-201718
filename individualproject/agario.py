import turtle
import time
import random
from ball import Ball

turtle.tracer(0,1)
turtle.hideturtle()

RUNNING=True
SLEEP= 0.0077
SCREEN_WIDTH= turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT= turtle.getcanvas().winfo_height()/2

MY_BALL=Ball(0,0,100, 500, 30/10,'blue')
NUMBER_OF_BALLS=5
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=100
MINIMUM_BALL_DX= -5
MAXIMUM_BALL_DX= 5
MINIMUM_BALL_DY= -5
MAXIMUM_BALL_DY= 5

BALLS= []

for new_ball in range(NUMBER_OF_BALLS):
	
	x=random.randint(round(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS), round(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS))
	
	dx=random.randint(round(MINIMUM_BALL_DX) , round(MAXIMUM_BALL_DX))
	while(dx==0):
		dx=random.randint(round(MINIMUM_BALL_DX), round(MAXIMUM_BALL_DX))
	
	y=random.randint(round(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS), round(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
	
	dy=random.randint(round(MINIMUM_BALL_DY), round(MAXIMUM_BALL_DY))
	while(dy==0):
		dy=random.randint(round(MINIMUM_BALL_DY), round(MAXIMUM_BALL_DY))	
	
	r=random.randint(round(MINIMUM_BALL_RADIUS) , round(MAXIMUM_BALL_RADIUS))
	
	color=(random.random(), random.random(), random.random())
	
	new_ball=Ball(x,y,dx,dy,r,color)

	BALLS.append(new_ball)

for ball in BALLS:
	ball.move(round(SCREEN_WIDTH), round(SCREEN_HEIGHT))

def collide(ball_a, ball_b):
	if ball_a==ball_b:
		return False
	#calculate.distance(ball_a.r , ball_b.r):
	distance= math.sqrt(math.pow((ball_a.r.MAXIMUM_BALL_RADIUS - ball_a.r.MINIMUM_BALL_RADIUS),2) + math.pow((ball_b.r.MAXIMUM_BALL_RADIUS - ball_b.r.MINIMUM_BALL_RADIUS),2))	
	if distance+10 <= (ball_a.r+ball_b.r):
		return True
	else:
		return False

def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if collide(ball_a, ball_b)==True:
				a_radius = ball_a.r
				b_radius = ball_b.r
				x=random.randint(round(-SCREEN_WIDTH), round(SCREEN_WIDTH))
				y=random.randint(round(-SCREEN_HEIGHT, round(SCREEN_HEIGHT)))
				r=random.randint(round(MINIMUM_BALL_RADIUS), round(MAXIMUM_BALL_RADIUS))
				color=(random.random(), random.random(), random.random())
				dx=random.randint(round(MINIMUM_BALL_DX), round(MAXIMUM_BALL_DX))
				dy=random.randint(round(MINIMUM_BALL_DY), round(MAXIMUM_BALL_DY))
				while (dx==0 and dy==0):
					dx=random.randint(round(MINIMUM_BALL_DX), round(MAXIMUM_BALL_DX))
					dy=random.randint(round(MINIMUM_BALL_DY), round(MAXIMUM_BALL_DY))

				if a_radius>=b_radius:



turtle.mainloop()

#def check_myball_collision():







