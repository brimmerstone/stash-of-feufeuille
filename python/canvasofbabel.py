from random import randint,choice
from turtle import Turtle, Screen, colormode

# Professor Æ. Ə. Gandha has taken over the Gallery of Babel!
# Fortunately, they kept all paintings safe and sound.
# They have given you magic canvas that can replicate a random painting from any corner of the gallery.
# And the best part? It lets you draw by locking the colors in tiles, although good luck trying to get a specific shade.


# USER MANUAL:
#   On tile:
#       LMB: Toggle tile lock
#       RMB: Check if tile is locked (the old fashioned way)
#   On background:
#       LMB: Regenerate unlocked tiles
#       RMB: Show only locked tiles (the better alternative)

s = 8 #shades
cv = int(256/s) #color value
colvals = [cv*i for i in range(s)] + [255]

wd,ln = 32,32
tile = 24
cols   = [[() for x in range(wd)] for y in range(ln)]
locked = [[0 for x in range(wd)] for y in range(ln)]

colormode(255)
t = Turtle()
t.hideturtle()
t.pensize(0)

w = Screen()
w.tracer(0)

stx = -wd/2*tile
sty = ln/2*tile
started = False
showlocked = False

def gettile(cx,cy):
    if started and cx > stx and cx < -stx and cy > -sty and cy < sty:
        tlx,tly = 0,0
        for dispx in range(int(stx),int(-stx),tile):
            if dispx+tile > cx:
                break
            tlx += 1
        for dispy in range(int(sty),int(-sty),-tile):
            if dispy-tile < cy:
                break
            tly += 1
        return tlx,tly
    else: return -1,-1

def draw(cx,cy):
    global started, locked

    if started and cx > stx and cx < -stx and cy > -sty and cy < sty:
        tlx,tly = gettile(cx,cy)
        locked[tly][tlx] = (locked[tly][tlx]+1)%2

    else:
        t.clear()
        t.teleport(stx,sty)
        for y in range(ln):
            for x in range(wd):
                if not locked[y][x]:
                    cols[y][x] = tuple(choice(colvals) for _ in range(3))
                t.color(cols[y][x])
                t.teleport(stx+x*tile,sty-y*tile)
                t.begin_fill()
                for N in range(4):
                    t.forward(tile)
                    t.right(90)
                t.end_fill()
        w.update()
        started = True

def rmbcheck(cx,cy):
    global showlocked

    if started and cx > stx and cx < -stx and cy > -sty and cy < sty:
        tlx,tly = gettile(cx,cy)
        if locked[tly][tlx]==0: n = "un"
        else: n = ""
        print(f"(X{tlx},Y{tly}) is {n}locked")

    elif not started:
        pass

    else:
        t.clear()
        t.teleport(stx, sty)
        if not showlocked:
            for y in range(ln):
                for x in range(wd):
                    t.teleport(stx + x * tile, sty - y * tile)
                    if locked[y][x]:
                        t.color(cols[y][x])
                        t.begin_fill()
                        for N in range(4):
                            t.forward(tile)
                            t.right(90)
                        t.end_fill()

        else:
            for y in range(ln):
                for x in range(wd):
                    t.color(cols[y][x])
                    t.teleport(stx + x * tile, sty - y * tile)
                    t.begin_fill()
                    for N in range(4):
                        t.forward(tile)
                        t.right(90)
                    t.end_fill()

        showlocked = (showlocked+1)%2
        w.update()

w.onscreenclick(rmbcheck,btn=3)
w.onscreenclick(draw,btn=1)
w.mainloop()