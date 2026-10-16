# conway's (PROPER DISPLAY, KINDA SLOW)
import turtle
from random import randint, choice
from datetime import datetime
from time import sleep

from golrules import*
from spawner import place

# SPAWN

for _ in range(int(round(WdT*LnT/4))):
    place(None,None,mapT)

# DISPLAY PART

scr = turtle.Screen()
scr.setup(width=1.0,height=1.0)
scr.bgcolor("black")
scr.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

tile = 16; delay = 0.02
scrWd, scrLn = tile*WdT, tile*LnT

t.teleport(-scrWd/2,scrLn/2)
t.pensize(2)

cords = [[],[]]

if DISPLAY_DEBUG:
    avgspeed = 0

def colTile(col):
    t.color(col)
    t.begin_fill()
    for _ in range(4):
        t.forward(tile)
        t.right(90)
    t.end_fill()

def Disp():
    global gen

    if SECRET_PARTY:
        gencolor = colors[gen%len(colors)]
    else:
        gencolor = "white"

    t.clear()
    t.teleport(-scrWd/2,scrLn/2)
    t.pensize(2)

    for y in range(LnT):
        for x in range(WdT):
            if x == 1:
                cords[0].append((t.pos()))
            elif x == 2:
                cords[1].append((t.pos()))

            if mapT[y][x] == 1:
                colTile(gencolor)
            t.teleport(t.pos()[0]+tile,t.pos()[1])
        pY = t.ycor()
        t.teleport(-scrWd/2,pY-tile)

    t.teleport(-scrWd/2,scrLn/2)
    t.pensize(10)
    t.color(gencolor)
    for _ in range(2):
        t.forward(scrWd)
        t.right(90)
        t.forward(scrLn)
        t.right(90)

    if gen == 1:
        print(cords[0])
        print(cords[1])
        print(-scrWd/2,scrLn/2)

    t.teleport(0,scrLn/2+50)
    live = len([_ for R in mapT for _ in R if _ == 1])
    t.write(str(f"{gen} | {live}"),align="center",font=("Lucida Console",32,"bold"))
    scr.update()

# CURSOR INTERACTION

def tileclick(x,y):
    global mapT,scrWd,scrLn

    if x < -scrWd/2 or x > scrWd/2 or y < -scrLn/2 or y > scrLn/2:
        return
    else:
        crX = -scrWd/2
        crY = scrLn/2
        Xt = 0
        Yt = 0
        while crX <= x:
            crX += tile
            Xt += 1
        while crY <= y:
            crY += tile
            Yt += 1
        place(Xt,Yt,mapT)

# SIMULATION PART

scr.onscreenclick(tileclick)
Disp()
prd1, prd2 = [], [] # these lists are used to break the cycle in case period-2 oscillators remain

while True:
    changes = 0
    if gen%3 == 0:
        prd1 = []
    if gen%3 == 2:
        prd2 = []
    for y in range(LnT):
        for x in range(WdT):
            alive=0
            for nb in neighbors:
                grid = mapT[(y+nb[0])%LnT][(x+nb[1])%WdT]
                alive += grid
            nmapT[y][x] = alive

    for y in range(LnT):
        for x in range(WdT):
            if mapT[y][x]==0 and nmapT[y][x] in rules["B"]:
                mapT[y][x]=1
                changes += 1
                if gen%3 == 0:
                    prd1.append((y,x))
                if gen%3 == 2:
                    prd2.append((y,x))


            elif mapT[y][x]==1 and nmapT[y][x] not in rules["S"]:
                mapT[y][x]=0
                changes += 1

    stagnant = True
    for y in range(LnT):
        if 1 in mapT[y]:
            stagnant = False
            break

    if prd1 == prd2 or changes == 0:
        stagnant = True

    # if SECRET_PARTY and gen%75==0:
    #     Spawner()

    if DISPLAY_DEBUG:
        if gen == 0:
            print(rulestring)
            print(f"{WdT*LnT} tiles total")
            t1 = datetime.now()
        else:
            t2 = datetime.now()
            diff = round(float(str(t2-t1)[5:]),4)
            print(f"{diff} seconds / {round(1/diff)} FPS")
            avgspeed += diff
            t1 = t2
    gen += 1
    Disp()

    if stagnant:
        break

if DISPLAY_DEBUG:
    avgspeed = round(avgspeed/gen,4)
    print(f"Average display speed: {avgspeed} seconds / {round(1/avgspeed)} FPS")

turtle.done()
turtle.exitonclick()