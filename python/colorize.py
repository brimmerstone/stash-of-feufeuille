from random import randint,choice
from turtle import Turtle, Screen, colormode

s = 8 #shades
cv = int(256/s) #color value

colvals = [32*i for i in range(s)] + [255]

debug = True
if debug:
    print(s+1, "shades")
    print(colvals)

def randcol():
    global colvals
    return choice(colvals)

wd,ln = 32,32
tile = 24

# for i in range(0,16,4):
#     for n in range(4):
#         print(cols[i+n],end=' ')
#     print()

colormode(255)
t = Turtle()
t.hideturtle()

w = Screen()
w.tracer(0)

stx = -wd/2*tile
sty = ln/2*tile

def randimg(fil,ler):
    t.clear()
    cols = [[tuple(randcol() for _ in range(3)) for _x in range(wd)] for _y in range(ln)]
    t.teleport(stx,sty)
    for y in range(ln):
        for x in range(wd):
            t.color(cols[y][x])
            t.teleport(stx+x*tile,sty-y*tile)
            t.begin_fill()
            for N in range(4):
                t.forward(tile)
                t.right(90)
            t.end_fill()
    w.update()

w.onscreenclick(randimg)
w.mainloop()