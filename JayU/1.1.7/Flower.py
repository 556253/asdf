#   a113_tower.py
#   Modify this code in VS Code to alternate the colors of the 
#   floors every three floors
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# start   ing location of the tower
x = -150
y = -150

# height of tower and a counter for each floor
num_floors = 63
floor = 0

# iterate
while floor < num_floors:
  # set placement and color of turtle
  painter.penup()
  if(floor%21==0):
    y=-150
    x=x+100
  painter.goto(x, y)
  if(floor%9>5):
    painter.color("red")
  elif(floor%9>2):
    painter.color("green")
  else:
    painter.color("blue")
  y = y + 5 # location of next floor
  floor = floor + 1
   
  #draw the floor
  painter.pendown()
  painter.forward(50)

wn = trtl.Screen()
wn.mainloop()