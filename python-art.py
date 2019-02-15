import turtle
import time
hecker  =  turtle.Turtle()

hecker.speed(0)
hecker.color("#917fe0")
def squarecircle():
    for i in range(128):
        for i in range(4):
            hecker.forward(70)
            hecker.right(90)
        hecker.right(2.8125)
        hecker.forward(1)
    hecker.up()
    hecker.forward(70)
    hecker.color("#b3bccc")
    hecker.down()
    for i in range(64):
        for i in range(4):
            hecker.forward(70)
            hecker.right(90)
        hecker.right(5.625)
        hecker.forward(1)
    hecker.up()
    hecker.backward(140)
    hecker.color("#b7a8e0")
    hecker.down()
    for i in range(32):
        for i in range(4):
            hecker.forward(70)
            hecker.right(90)
        hecker.right(11.25)
        hecker.forward(1)
    hecker.left(90)
    hecker.up()
    hecker.backward(245)
    hecker.left(90)
    hecker.forward(175)
    hecker.right(90)
    hecker.color("#f6d4f7")
    for i in range(35):
        for i in range(35):
            hecker.dot()
            hecker.forward(15)
        hecker.backward(525)
        hecker.right(90)
        hecker.forward(15)
        hecker.left(90)
        
squarecircle()
time.sleep(4)
