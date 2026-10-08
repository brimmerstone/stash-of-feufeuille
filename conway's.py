# conway's (PROPER DISPLAY, KINDA SLOW)
import turtle
from time import sleep
from random import randint, choice
from datetime import datetime

Wd, Ln = 32,32
gen = 0

rulestring = "B3/S23"
rules = {}
for i in range(2):
    rules[rulestring.split("/")[i][0]] = [int(n) for n in rulestring.split("/")[i] if n.isdigit()]

"""
rules["B"] — Bear:    0 to 1
rules["S"] — Survive: 1 to 1
else       — Die:     1 to 0
"""

map = [[0 for X in range(Wd)] for Y in range(Ln)]
nbmap = [[0 for X in range(Wd)] for Y in range(Ln)]

def place(x=None,y=None):
    if x is None:
        x = randint(0,Wd)
    if y is None:
        y = randint(0,Ln)
    map[y%Ln][x%Wd] = 1
    return map[y%Ln][x%Wd]

neighbors = [[-1,-1],[-1,0],[-1,1],
             [ 0,-1],       [ 0,1],
             [ 1,-1],[ 1,0],[ 1,1]]

diagDirs = ['ne','nw','se','sw']
Dirs = ['l','r','u','d']

def Spawner(ptn=None,x=None,y=None):

    patterns = ['glider_ne','glider_nw','glider_se','glider_sw',
                'spaceship_l','spaceship_r','spaceship_u','spaceship_d',
                'r_pentomino','beacon1','beacon2','block','clock']

    base = ['glider','spaceship']

    if x is None:
        x = randint(0,Wd-1)
    if y is None:
        y = randint(0,Ln-1)

    if ptn:
        ptn = ptn.lower()
    if ptn not in patterns or ptn not in base:
        ptn = choice(patterns)

    if ptn in base:
        match ptn:
            case 'glider':
                ptn += '_' + choice(diagDirs)
            case 'spaceship':
                ptn += '_' + choice(Dirs)

    match ptn:
        case 'block':
            for X in range(2):
                for Y in range(2):
                    place(x+X,y+Y)

        case 'glider_ne':
            place(x+1,y); place(x,y+1)
            place(x-1,y-1); place(x,y-1); place(x+1,y-1)
        case 'glider_nw':
            place(x-1,y); place(x,y+1)
            place(x-1,y-1); place(x,y-1); place(x+1,y-1)
        case 'glider_se':
            place(x,y-1); place(x+1,y)
            place(x-1,y+1); place(x,y+1); place(x+1,y+1)
        case 'glider_sw':
            place(x,y-1); place(x-1,y)
            place(x-1,y+1); place(x,y+1); place(x+1,y+1)

        case 'r_pentomino':
            place(x,y-1); place(x+1,y-1)
            place(x-1,y); place(x,y); place(x,y+1)

        case 'spaceship_l':
            place(x-1,y-1); place(x+2,y-1); place(x-2,y)
            place(x-2,y+1); place(x+2,y+1)
            for N in range(4):
                place(x-2+N,y+2)
        case 'spaceship_r':
            place(x-2,y-1);place(x+1,y-1); place(x+2,y)
            place(x-2,y+1);place(x+2,y+1)
            for N in range(4):
                place(x-1+N,y+2)
        case 'spaceship_u':
            for N in range(3):
                place(x+N,y-2)
            for N in range(3):
                place(x+2,y-1+N)
            place(x-1,y-1); place(x-1,y+2); place(x+1,y+2)
        case 'spaceship_d':
            for N in range(3):
                place(x-2,y-1+N)
            for N in range(3):
                place(x-2+N,y+2)
            place(x-1,y-2); place(x+1,y-2); place(x+1,y+1)

        case 'beacon1':
            for N in range(2):
                for X in range(2):
                    for Y in range(2):
                        place(x+X+N*2,y+Y+N*2)
        case 'beacon2':
            for X in range(2):
                for Y in range(2):
                    place(x+X+2,y+Y)
                    place(x+X,y+Y+2)

        case 'clock':
            Spawner('block',x+1,y-5)
            Spawner('block',x-5,y-1)
            Spawner('block',x+5,y+1)
            Spawner('block',x-1,y+5)
            for N in range(4):
                place(x-1+N,y-2)
                place(x-1+N,y+3)
                place(x-2,y-1+N)
                place(x+3,y-1+N)
            place(x,y+1); place(x,y); place(x+1,y-1)

# SPAWN

for _ in range(int(round(Wd*Ln/4))):
    place()

# DISPLAY PART

scr = turtle.Screen()
scr.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

tile = 16; delay = 0.02
scrWd, scrLn = tile*Wd, tile*Ln

t.teleport(-scrWd/2,scrLn/2)
t.pensize(2)

DISPLAY_DEBUG = 1
SECRET_PARTY  = 0

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

    colors = ["#C00000","#C03000","#C06000","#C09000",
              "#C0C000","#90C000","#60C000","#30C000",
              "#00C000","#00C030","#00C060","#00C090",
              "#00C0C0","#0090C0","#0060C0","#0030C0",
              "#0000C0","#3000C0","#6000C0","#9000C0",
              "#C000C0","#C00090","#C00060","#C00030"]
    if SECRET_PARTY:
        gencolor = colors[gen%len(colors)]
    else:
        gencolor = "black"

    t.clear()
    t.teleport(-scrWd/2,scrLn/2)
    t.pensize(2)

    for y in range(Ln):
        for x in range(Wd):
            if map[y][x] == 1:
                colTile(gencolor)
            else:
                colTile("white")
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

    t.teleport(0,scrLn/2+50)
    live = len([_ for R in map for _ in R if _ == 1])
    t.write(str(f"{gen} | {live}"),align="center",font=("Lucida Console",32,"bold"))
    scr.update()

# SIMULATION PART

Disp()
prd1, prd2 = [], [] # these lists are used to break the cycle in case period-2 oscillators remain

while True:
    changes = 0
    if gen%3 == 0:
        prd1 = []
    if gen%3 == 2:
        prd2 = []
    for y in range(Ln):
        for x in range(Wd):
            alive=0
            for nb in neighbors:
                grid = map[(y+nb[0])%Ln][(x+nb[1])%Wd]
                alive += grid
            nbmap[y][x] = alive

    for y in range(Ln):
        for x in range(Wd):
            if map[y][x]==0 and nbmap[y][x] in rules["B"]:
                map[y][x]=1
                changes += 1
                if gen%3 == 0:
                    prd1.append((y,x))
                if gen%3 == 2:
                    prd2.append((y,x))


            elif map[y][x]==1 and nbmap[y][x] not in rules["S"]:
                map[y][x]=0
                changes += 1

    stagnant = True
    for y in range(Ln):
        if 1 in map[y]:
            stagnant = False
            break

    if prd1 == prd2 or changes == 0:
        stagnant = True

    # if SECRET_PARTY and gen%75==0:
    #     Spawner()

    if DISPLAY_DEBUG:
        if gen == 0:
            print(rulestring)
            print(f"{Wd*Ln} tiles total")
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

avgspeed = round(avgspeed/gen,4)
print(f"Average display speed: {avgspeed} seconds / {round(1/avgspeed)} FPS")

turtle.done()
turtle.exitonclick()
