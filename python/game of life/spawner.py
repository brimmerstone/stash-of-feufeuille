from golrules import*
from random import randint,choice

def place(x=None,y=None,map=gmmap):
    if x is None:
        if map == gmmapT:
            x = randint(0, WdT)
        else:
            x = randint(0,Wd)
    if y is None:
        if map == gmmapT:
            y = randint(0, LnT)
        else:
            y = randint(0,Ln)

    if map == gmmapT:
        map[y%LnT][x%WdT] = 1
        return map[y%LnT][x%WdT]
    else:
        map[y%Ln][x%Wd] = 1
        return map[y%Ln][x%Wd]

def spawnentity(ptn=None,x=None,y=None):

    diagdirs = ['ne', 'nw', 'se', 'sw']
    dirs = ['l', 'r', 'u', 'd']
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
                ptn += '_' + choice(diagdirs)
            case 'spaceship':
                ptn += '_' + choice(dirs)

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
            spawnentity('block',x+1,y-5)
            spawnentity('block',x-5,y-1)
            spawnentity('block',x+5,y+1)
            spawnentity('block',x-1,y+5)
            for N in range(4):
                place(x-1+N,y-2)
                place(x-1+N,y+3)
                place(x-2,y-1+N)
                place(x+3,y-1+N)
            place(x,y+1); place(x,y); place(x+1,y-1)