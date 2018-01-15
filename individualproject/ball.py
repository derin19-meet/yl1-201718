from turtle import *



class Ball(Turtle):
    def __init__(self,x,y,dx,dy,r,color):
        Turtle.__init__(self)
        self.penup()
        self.x=x
        self.y=y
        self.dx=dx
        self.dy=dy
        self.r=r
        self.color(color)
        self.shape('circle')

    def move(self, screen_width, screen_height):
        self.screen_width=screen_width
        self.screen_height=screen_height
        current_x= self.xcor()
        new_x= current_x + self.dx
        current_y= self.ycor()
        new_y= current_y + self.dy

        self.goto(new_x, new_y)
                
        right_side_ball= new_x + self.r
        left_side_ball= new_x - self.r
        top_side_ball= new_y + self.r
        bottom_side_ball= new_y - self.r

        if top_side_ball>= screen_height/2:
            self.goto(self.dx,-self.dy)
        if bottom_side_ball>= -screen_height/2:
                self.goto(self.dx, self.dy)
        if left_side_ball>= -screen_width/2:
                self.goto(self.dx, -self.dy)
        if right_side_ball>= screen_width/2:
                self.goto(self.dx,self.dy)
        


a= Ball(0,0,100, 500, 10/10,'blue')
flag = True
while flag:
    a.move(500,500)


