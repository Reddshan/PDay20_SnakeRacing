from turtle import Turtle , Screen
STARTING_POS=[(20, 0), (0, 0), (-20, 0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:

    def __init__(self):
        self.head = None
        self.name="hello"
        self.objlst=[]
        self.create_snake()

    def create_snake(self):
        for pos in STARTING_POS:
            self.add_obj(pos)
        self.head = self.objlst[0]
    def add_obj(self,pos):
        turobj = Turtle(shape="square")
        turobj.color("white")
        turobj.penup()
        turobj.goto(pos)
        self.objlst.append(turobj)

    def extend(self):
        self.add_obj(self.objlst[-1].position())
    def move(self):

        for seg_num in range(len(self.objlst) - 1, 0, -1):
            new_x = self.objlst[seg_num - 1].xcor()
            new_y = self.objlst[seg_num - 1].ycor()
            self.objlst[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading()!=DOWN:
           self.head.setheading(90)
           #self.move()
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
            #self.move()
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
            #self.move()
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
            #self.move()