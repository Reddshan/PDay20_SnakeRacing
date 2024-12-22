import time
from turtle import Turtle , Screen
from snake import Snake
from food import Food
from score import Score

scr=Screen()
######  Objects declaration
sn=Snake()
fd=Food()
sr=Score()
##sn.create_snake()

### Screens setup
scr.setup(width=600,height=600)

scr.title("My Snake Game")
scr.tracer(0)
scr.bgcolor("black")
scr.listen()

##### Keys setup
scr.onkey(sn.up,"Up")
scr.onkey(sn.down,"Down")
scr.onkey(sn.left,"Left")
scr.onkey(sn.right,"Right")

#fd.place_pos()



##starting_pos=[(0,0),(20,0),(-20,0)]

is_run=True

while is_run:
    scr.update()
    time.sleep(0.1)
    sn.move()
    ### detects collision  with food and adds score
    if sn.head.distance(fd)<15:
        fd.refresh()
        sn.extend()
        sr.score_add()
        ##print(f"Your Score:{sr.score}")
    ### detects collision with wall and becomes game over
    if sn.head.xcor()>290 or sn.head.xcor()<-290 or sn.head.ycor()<-290 or sn.head.ycor()>290  :
        sr.game_over()
        is_run=False
    ### detect collision with tail
    for obj1 in sn.objlst[1:]:
        # if obj1 == sn.objlst[0]:
        #     pass
        if sn.objlst[0].distance(obj1)<10:
            is_run=False
            sr.game_over()





# #turobj1=Turtle(shape="square")
# turobj1.color("white")
#
# turobj2=Turtle(shape="square")
# turobj2.color("white")
# turobj2.setpos(x=-20,y=0)
# #turobj

scr.exitonclick()