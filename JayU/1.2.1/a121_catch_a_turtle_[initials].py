# a121_catch_a_turtle.py

#-----import statements-----
import turtle as trtl
import random as rand

#-----initialize turtle-----
v = trtl.Turtle()
v_color = "blue"
v_shape = "turtle"
v.speed(0)

sw=trtl.Turtle()
sw.pendown()
sw.hideturtle()
sw.setposition(-180,180)
sw.showturtle()
for i in range(2):
  sw.forward(50)
  sw.right(90)
  sw.forward(20)
  sw.right(90)

#-----game configuration----
v.shape(v_shape)
v.shapesize(1,1,0)
v.fillcolor(v_color)
score=0

#-----game functions--------
def change_pos():
  x=rand.randint(-200,200)
  y=rand.randint(-150,150)
  v.hideturtle()
  v.setposition(x,y)
  v.showturtle()

def update_score():
  global score
  score+=1
  print(score)

def v_clicked(x,y):
  update_score()
  change_pos()



#-----events----------------
v.penup()
v.onclick(v_clicked)

wn = trtl.Screen()
wn.mainloop()

