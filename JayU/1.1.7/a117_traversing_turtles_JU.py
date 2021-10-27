#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)
  new_color = turtle_colors.pop() 
  t.fillcolor(new_color)
  t.pencolor(new_color)

#  Starting position
startx = 0
starty = 0
direction=90
# Positioning each shape
for t in my_turtles:
  t.penup()
  t.goto(startx, starty)
  t.setheading(direction)
  t.right(45)
  t.pendown()     
  t.forward(50)
  direction=t.heading()

#	changing the location of each shape everytime
  startx = t.xcor()
  starty = t.ycor()

wn = trtl.Screen()
wn.mainloop()