import turtle

def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-5,t)
        t.left(40)
        t.color("green")
        tree(branchLen-5,t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(166)
    t.down()
    t.color("brown")
    tree(75,t)
    myWin.exitonclick()

main()
