#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold

#Name
# Tim Carpenter
#Date
# 12/19/19

#### INSTRUCTIONS ####
#Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller
#u should pick the pen up or put the pen down
#All code must be commented
#BONUS
#Add a feature to change colors

#import required libraries
import turtle as trtl

#create turtles
pen = trtl.Turtle(visible = False)
pen._delay(0)
pen.speed(0)

#this turtle gives the clearScreen function a top-down wipe effect instead of just being instantaneous
clearT = trtl.Turtle(shape = "square", visible = False)
clearT.shapesize(100)
clearT.seth(270)
clearT.color("gainsboro")
clearT.speed(0)
clearT.pu()
clearT.goto(0, 1600)
clearT.st()

#this turtle just makes a box around the indacators
boxT = trtl.Turtle(visible = False)
boxT.pu()
boxT.goto(-1000, -110)
boxT.pd()
boxT.pensize(1.5)
boxT.fd(125)
boxT.right(90)
boxT.fd(500)

#this turtle is for telling you what the pen currently looks like
penIndicator = trtl.Turtle(visible = False)
penIndicator.pu()
penIndicator._delay(0)
penIndicator.goto(-925, -150)
penIndicator.pd()

#lists for colorGuide to pull from
colorGuideColors = ["pink", "brown", "orange", "purple", "yellow", "green", "blue", "red", "white", "black"]
colorGuideNumbers = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#this turtle tells you which key is which color
colorGuide = trtl.Turtle(visible = False)
colorGuide.pu()
colorGuide._delay(0)
colorGuide.goto(-925, -225)

#draw the color guide
for i in range(10):
    colorGuideColor = colorGuideColors.pop()
    colorGuideNumber = colorGuideNumbers.pop()
    colorGuide.color(colorGuideColor)
    colorGuide.write(colorGuideNumber, font = ("Arial", 20, "normal"))
    colorGuide.sety(colorGuide.ycor() - 25)

#movement functions

def left():
    if pen.xcor() > -865: #can't leave the screen
        pen.seth(180)
        pen.fd(10)
def right():
    if pen.xcor() < 925:
        pen.seth(0)
        pen.fd(10)
def up():
    if pen.ycor() < 520:
        pen.seth(90)
        pen.fd(10)
def down():
    if pen.ycor() > -500:
        pen.seth(270)
        pen.fd(10)

#color/drawing functions

pd = True #variable for if the pen is down
ps = 1 #variable for pensize

penIndicator.pensize(ps)
penIndicator.clear()
penIndicator.fd(10)
penIndicator.pu()
penIndicator.back(10)
penIndicator.pd()

def increasePensize():
    global ps
    ps += 0.5
    pen.pensize(ps)
    penIndicator.pensize(ps)
    penIndicator.clear()
    penIndicator.fd(10)
    penIndicator.pu()
    penIndicator.back(10)
    penIndicator.pd()
def decreasePensize():
    global ps
    ps -= 0.5
    pen.pensize(ps)
    penIndicator.pensize(ps)
    penIndicator.clear()
    penIndicator.fd(10)
    penIndicator.pu()
    penIndicator.back(10)
    penIndicator.pd()
def togglePen():
    global pd
    if pd == True:
        pen.pu()
        pd = False
    else:
        pen.pd()
        pd = True
def clearScreen():
    for i in range(230): #moves clearT down to "wipe" the screen
        clearT.fd(5)
    pen.clear() #once clearT is covering the screen, clear the drawing
    clearT.goto(0, 1600) #return clearT to its original position
    #I could've just used pen.clear() but that's boring
def black():
    pen.pencolor("black")
    penIndicator.pencolor("black")
    penIndicator.clear()
    penIndicator.fd(10)
    penIndicator.pu()
    penIndicator.back(10)
    penIndicator.pd()
def white():
    pen.pencolor("white")
    penIndicator.pencolor("white")
    penIndicator.clear()
    penIndicator.fd(10)
    penIndicator.pu()
    penIndicator.back(10)
    penIndicator.pd()
def red():
    pen.pencolor("red")
    penIndicator.pencolor("red")
    penIndicator.clear()
    penIndicator.fd(10)
    penIndicator.pu()
    penIndicator.back(10)
    penIndicator.pd()
def blue():
    pen.pencolor("blue")
    penIndicator.pencolor("blue")
    penIndicator.clear()
    penIndicator.fd(10)
    penIndicator.pu()
    penIndicator.back(10)
    penIndicator.pd()
def green():
    pen.pencolor("green")
    penIndicator.pencolor("green")
    penIndicator.clear()
    penIndicator.fd(10)
    penIndicator.pu()
    penIndicator.back(10)
    penIndicator.pd()
def yellow():
    pen.pencolor("yellow")
    penIndicator.pencolor("yellow")
    penIndicator.clear()
    penIndicator.fd(10)
    penIndicator.pu()
    penIndicator.back(10)
    penIndicator.pd()
def purple():
    pen.pencolor("purple")
    penIndicator.pencolor("purple")
    penIndicator.clear()
    penIndicator.fd(10)
    penIndicator.pu()
    penIndicator.back(10)
    penIndicator.pd()
def orange():
    pen.pencolor("orange")
    penIndicator.pencolor("orange")
    penIndicator.clear()
    penIndicator.fd(10)
    penIndicator.pu()
    penIndicator.back(10)
    penIndicator.pd()
def brown():
    pen.pencolor("brown")
    penIndicator.pencolor("brown")
    penIndicator.clear()
    penIndicator.fd(10)
    penIndicator.pu()
    penIndicator.back(10)
    penIndicator.pd()
def pink():
    pen.pencolor("pink")
    penIndicator.pencolor("pink")
    penIndicator.clear()
    penIndicator.fd(10)
    penIndicator.pu()
    penIndicator.back(10)
    penIndicator.pd()

#create screen
wn = trtl.Screen()
wn.setup(width = 1.0, height = 1.0)
wn.bgcolor("gainsboro")

#bind to keypresses
wn.onkeypress(left, "a")
wn.onkeypress(right, "d")
wn.onkeypress(up, "w")
wn.onkeypress(down, "s")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(increasePensize, "o")
wn.onkeypress(decreasePensize, "p")
wn.onkeypress(togglePen, "u")
wn.onkeypress(clearScreen, "space")
wn.onkeypress(black, "1")
wn.onkeypress(white, "2")
wn.onkeypress(red, "3")
wn.onkeypress(blue, "4")
wn.onkeypress(green, "5")
wn.onkeypress(yellow, "6")
wn.onkeypress(purple, "7")
wn.onkeypress(orange, "8")
wn.onkeypress(brown, "9")
wn.onkeypress(pink, "0")

#listen
wn.listen()

#mainloop
wn.mainloop()
