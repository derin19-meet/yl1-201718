import turtle

turtle.shape('circle')
turtle.tracer(1,0)

class Ball(object):
	def__init__(self,x,y,shape,dx,dy,r,color)
		self.x=x
		self.y=y
		self.dx=dx
		self.dy=dy
		self.r=r
		self.color=color
a= Ball(0,0,'circle',100, 500, r/10,'blue')

turtle.penup()

class move(object):
	def__init__(self, screen_width, screen_height)
		self.screen_width=screen_width
		self.screen_height=screen_height
	current_x=[0]
	new_x= self.current_x + self.move(dx)
	current_y=[0]
	new_y= self.current_y + self.move(dy)
	right_side_ball= new_x + self.move(r)
	left_side_ball= new_x - self.move(r)
	top_side_ball= new_y + self.move(r)
	bottom_side_ball= new_y - self.move(r)
self.goto(new_x, new_y)
turtle.mainloop()
