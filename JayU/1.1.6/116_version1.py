#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
spider.goto(0,0)
spider.pensize(40)
spider.circle(20)
legs = 8
length = 70
direction = 360/legs
spider.pensize(5)
leg_counter = 0
while (leg_counter < legs):
  spider.goto(0,20)
  if(leg_counter < 4):
    spider.setheading(direction * leg_counter - leg_counter * 22.5)
  else:
    spider.setheading(direction * leg_counter + 90 - leg_counter * 22.5)
  spider.forward(length)
  leg_counter = leg_counter + 1

wn = trtl.Screen()
wn.mainloop()