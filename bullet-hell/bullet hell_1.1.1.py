import pygame
import csv
from random import randint

WIDTH = 800; LENGTH = 600
pygame.init()
screen = pygame.display.set_mode((WIDTH, LENGTH))
pygame.display.set_caption("FL's Average Bullet Hell")
PLX = WIDTH // 2; PLY = LENGTH // 2; SIZE = 20
AUX = -500; AUY = -500
clock = pygame.time.Clock()
run = True; game = False; started = False; showtip = True
score = 0; speed = 5; bulletspeed = 5;
lastkey = '' ; inertia = 5
font = pygame.font.SysFont('Consolas', 36)
font2 = pygame.font.SysFont('Consolas',72)
font3 = pygame.font.SysFont('Consolas',16)

visible = False
appeartime = 0
duration = 500
cooldown = 750
lastpress = 0

spawn = 15
bullets = []; bulletsR = []; bulletsU = []; bulletsD = []
parried = []; parriedR = []; parriedU = []; parriedD = []
bGROUP = [bullets,bulletsR,bulletsU,bulletsD]
pGROUP = [parried,parriedR,parriedU,parriedD]

data = []
with open('scores.csv','r',newline='') as fl:
    file = csv.reader(fl)
    for row in file:
        data.append(row)

def loaddata():
    global spawn, score, highscore, data
    if spawn == 25:
        highscore = int(data[0][0])
    if spawn == 15:
        highscore = int(data[1][0])
    if spawn == 10:
        highscore = int(data[2][0])
    if spawn == 6:
        highscore = int(data[3][0])

def savedata():
    global spawn,score,highscore,data
    if highscore < score:
        highscore = score
    if spawn == 25:
        data[0][0] = str(highscore)
    if spawn == 15:
        data[1][0] = str(highscore)
    if spawn == 10:
        data[2][0] = str(highscore)
    if spawn == 6:
        data[3][0] = str(highscore)
    with open('scores.csv','w',newline='') as fl:
        writer = csv.writer(fl)
        writer.writerows(data)

def Scored():
    global score,highscore
    score += 1
    if score > highscore:
        highscore = score
        savedata()

loaddata()
while run:
    aura = pygame.Rect(AUX,AUY, SIZE * 2, SIZE * 2)
    player = pygame.Rect(PLX, PLY, SIZE, SIZE)
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            savedata()
            run = False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                current = pygame.time.get_ticks()
                if current - lastpress > cooldown:
                    visible = True
                    AUX = PLX - (SIZE // 2); AUY = PLY - (SIZE // 2)
                    appeartime = pygame.time.get_ticks()
                    lastpress = current

            if event.key == pygame.K_RETURN and not started:
                started = True
                game = True

            if event.key == pygame.K_RETURN and not game and started:
                PLX, PLY = WIDTH // 2, LENGTH // 2
                AUX = -1000; AUY = -1000
                visible = False
                score = 0
                savedata()
                for group in bGROUP + pGROUP:
                    group.clear()
                game = True

            if event.key == pygame.K_1 and not game:
                bulletspeed = 4
                duration = 750
                cooldown = 500
                spawn = 25
            if event.key == pygame.K_2 and not game:
                bulletspeed = 5
                duration = 500
                cooldown = 750
                spawn = 15
            if event.key == pygame.K_3 and not game:
                bulletspeed = 5
                duration = 500
                cooldown = 1000
                spawn = 10
            if event.key == pygame.K_4 and not game:
                bulletspeed = 6
                duration = 500
                cooldown = 1000
                spawn = 6
            if event.key == pygame.K_0 and not game:
                if showtip:
                    showtip = False
                else:
                    showtip = True
            loaddata()

    if game:
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and PLX - speed >= 0:
            PLX -= speed
            lastkey = 'LEFT'
            inertia = 5
            if visible:
                AUX -= speed
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and PLX + speed <= WIDTH-SIZE:
            PLX += speed
            lastkey = 'RIGHT'
            inertia = 5
            if visible:
                AUX += speed
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and PLY - speed >= 0:
            PLY -= speed
            lastkey = 'UP'
            inertia = 5
            if visible:
                AUY -= speed
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and PLY + speed <= LENGTH-SIZE:
            PLY += speed
            lastkey = 'DOWN'
            inertia = 5
            if visible:
                AUY += speed
        if not any(keys):
            if inertia>0:
                if lastkey == 'LEFT' and PLX - speed >= 0:
                    PLX -= int(inertia)
                    AUX -= int(inertia)
                if lastkey == 'RIGHT' and PLX + speed <= WIDTH-SIZE:
                    PLX += int(inertia)
                    AUX += int(inertia)
                if lastkey == 'UP' and PLY - speed >= 0:
                    PLY -= int(inertia)
                    AUY -= int(inertia)
                if lastkey == 'DOWN' and PLY + speed <= LENGTH-SIZE:
                    PLY += int(inertia)
                    AUY += int(inertia)
                inertia -= 1
        if visible:
            if pygame.time.get_ticks() - appeartime > duration:
                AUX = -1000; AUY = -1000
                visible = False

        if randint(1,spawn)==1:
            bullets.append(pygame.Rect(-75,randint(0,LENGTH),25,5))
        if randint(1,spawn)==1:
            bulletsR.append(pygame.Rect(1000,randint(0,LENGTH),25,5))
        if randint(1,spawn)==1:
            bulletsU.append(pygame.Rect(randint(0,WIDTH),-75,5,25))
        if randint(1,spawn)==1:
            bulletsD.append(pygame.Rect(randint(0,WIDTH),800,5,25))

        for group in bGROUP+pGROUP:
            for bullet in group:
                if group == bullets or group == parriedR:
                    bullet.x += bulletspeed
                    if bullet.x > LENGTH + 200:
                        group.remove(bullet)
                        Scored()
                if group == bulletsR or group == parried:
                    bullet.x -= bulletspeed
                    if bullet.x < -75:
                        group.remove(bullet)
                        Scored()
                if group == bulletsU or group == parriedD:
                    bullet.y += bulletspeed
                    if bullet.y > 800:
                        group.remove(bullet)
                        Scored()
                if group == bulletsD or group == parriedU:
                    bullet.y -= bulletspeed
                    if bullet.y < -75:
                        group.remove(bullet)
                        Scored()
                if player.colliderect(bullet) and group in bGROUP:
                    savedata()
                    game = False
                    pygame.time.delay(500)
                    score = 0
                if aura.colliderect(bullet) and group in bGROUP:
                    if group == bullets:
                        parried.append(bullet)
                    if group == bulletsR:
                        parriedR.append(bullet)
                    if group == bulletsU:
                        parriedU.append(bullet)
                    if group == bulletsD:
                        parriedD.append(bullet)
                    group.remove(bullet)
                    Scored()

    screen.fill((0,0,0))
    if game:
        if visible:
            pygame.draw.rect(screen, (192,192,192),aura)
        pygame.draw.rect(screen, (255, 255, 255), player)
        for group in bGROUP:
            for bullet in group:
                pygame.draw.rect(screen,(255,64,64),bullet)
        for group in pGROUP:
            for bullet in group:
                pygame.draw.rect(screen,(255,255,255),bullet)
    score_text = font.render(f"Score: {score}", True, (255,255,255))
    sbox = score_text.get_rect(topleft=(10,10))
    highscoretext = font.render(f"High Score: {highscore}", True, (255,255,255))
    hsbox = highscoretext.get_rect(topright=(790,10))
    screen.blit(highscoretext,hsbox)
    screen.blit(score_text, (10, 10))
    if not game:
        if not started:
            startgame = font.render('PRESS ENTER TO START',True,(255,255,255))
            thebox = startgame.get_rect(center=(WIDTH//2,LENGTH//2))
            screen.blit(startgame,thebox)
        else:
            gameover = font2.render("GAME OVER",True,(255,255,255))
            textbox = gameover.get_rect(center=(WIDTH // 2, LENGTH // 2))
            restart = font.render("PRESS ENTER TO RESTART",True,(255,255,255))
            textbox2 = gameover.get_rect(center=((WIDTH // 2)-40, (LENGTH//2)+60))
            screen.blit(gameover,textbox)
            screen.blit(restart,textbox2)
        if spawn == 25:
            diff = font3.render('EASY',True,(0,255,0))
        if spawn == 15:
            diff = font3.render('NORMAL',True,(255,255,0))
        if spawn == 10:
            diff = font3.render('HARD',True,(255,0,0))
        if spawn == 6:
            diff = font3.render('BULLET HELL',True,(128,0,0))
        diffbox = diff.get_rect(topright=(790,50))
        screen.blit(diff,diffbox)
        if showtip:
            tip1 = font3.render('Press SHIFT to parry bullets around you.',True,(255,255,255))
            screen.blit(tip1,(10,555))
            tip2 = font3.render('You can change the game difficulty via number keys. (press 0 to hide tips)',True,(255,255,255))
            screen.blit(tip2,(10,575))

    pygame.display.update()
pygame.quit()

# FL's average bullet hell 1.1.1 FLABH
# 1.1.1 - added inertia, tips are now hideable
# 1.1   - added restart feature, game over screen, difficulties, difficulty indicator, highscore per difficulty system, tips, optimized some of the code, slight changes in settings
# 1.0.2 - added bullets to other sides
# 1.0.1 - added interception/parrying
