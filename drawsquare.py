import turtle

def drawTriangle():
    mark = turtle.Turtle()
    mark.shape("turtle")
    mark.color("black")
    mark.speed(2)
    i = 0
    while i < 3:
        mark.right(120)
        mark.forward(100)
        i += 1
        
def drawCircle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("red")
    angie.circle(100)

def drawSquare(turtleName):
    i = 0
    while i < 4:
        turtleName.forward(100)
        turtleName.right(90)
        i += 1
        
def drawArt():
    window = turtle.Screen()
    window.bgcolor("blue")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.speed(.2)
    brad.color("black")
    for i in range(1,37):
        drawSquare(brad)
        brad.right(10)
    window.exitonclick()
    
drawArt()
