import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
            myTurtle.forward(lineLen)
            myTurtle.right(1)
            drawSpiral(myTurtle,lineLen-0.001)
drawSpiral(myTurtle,25)
myWin.exitonclick()
          

