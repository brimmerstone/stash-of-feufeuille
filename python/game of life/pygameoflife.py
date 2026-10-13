import pygame
from random import randint, choice
from spawner import place
from golrules import*

pygame.init()

WIDTH = 1024; LENGTH = 512+256

screen = pygame.display.set_mode((WIDTH, LENGTH))
pygame.display.set_caption("Conway's PyGame of Life")
clock = pygame.time.Clock()

for _ in range(int(round(Wd*Ln/4))):
    place()

# DISPLAY GOES BELOW



ts = 5
offset = 200
def display():
    for y in range(Ln):
        for x in range(Wd):
            tile = pygame.Rect(offset+ts*x,offset+ts*y,ts,ts)
            if gmmap[y][x] == 1:
                pygame.draw.rect(screen, (255,255,255),tile)
            else:
                pygame.draw.rect(screen, (0,0,0),tile)
    pygame.display.flip()

# LOGIC DOES BELOW (should've been relocated to golrules.py)

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
                grid = gmmap[(y+nb[0])%Ln][(x+nb[1])%Wd]
                alive += grid
            nbmap[y][x] = alive

    for y in range(Ln):
        for x in range(Wd):
            if gmmap[y][x]==0 and nbmap[y][x] in rules["B"]:
                gmmap[y][x]=1
                changes += 1
                if gen%3 == 0:
                    prd1.append((y,x))
                if gen%3 == 2:
                    prd2.append((y,x))


            elif gmmap[y][x]==1 and nbmap[y][x] not in rules["S"]:
                gmmap[y][x]=0
                changes += 1

    stagnant = True
    for y in range(Ln):
        if 1 in gmmap[y]:
            stagnant = False
            break

    if prd1 == prd2 or changes == 0:
        stagnant = True

    gen += 1
    display()

    if stagnant:
        break