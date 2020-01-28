import pygame as py
import random
py.init()
disp_w = 1200
disp_h = 600
font = py.font.SysFont(None,40,True)
font2 = py.font.SysFont(None,60)
font1 = py.font.SysFont(None,30,True)

def score(count):
    screen_text = font1.render("Score:%d"%count, True, red)
    gameDisplay.blit(screen_text, [1070,30])

def snake(body):
    for i in body:
        py.draw.rect(gameDisplay, red, [i[0], i[1], 20, 20])

def mgameover(msg,color):
    screen_text = font.render(msg,True,color)
    gameDisplay.blit(screen_text,[disp_w/2-disp_h/4,disp_h/2])

def tstartscreen():
    screen_text = font2.render("1.Start",True,blue)
    gameDisplay.blit(screen_text,[disp_w/2-disp_h/4,disp_h/2-50])

def texit():
    screen_text = font2.render("2.Exit",True,blue)
    gameDisplay.blit(screen_text,[disp_w/2-disp_h/4,disp_h/2+10])


gameDisplay = py.display.set_mode((disp_w,disp_h))
py.display.set_caption('Catch The Owl')

red = (255,0,0)
black =(0,0,0)
blue = (64,0,255)

clock = py.time.Clock()
gameover = False

def gamemain():
    gameExit = False
    gameover = False
    count =0
    x = disp_w / 2
    y = disp_h / 2
    x1 = round(random.randrange(0,disp_w-20)/20.0)*20.0
    y1 = round(random.randrange(0,disp_h-20)/20.0)*20.0
    cx = 0
    cy = 0
    xandyelement = []
    basketlength = 1
    fps = 10
    score(count)
    py.display.update()
    while not  gameExit:
        while gameover == True:
            mgameover("Retry Press R or Any other Key To Exit", red)
            py.display.update()
            for e in py.event.get():
                if e.type == py.KEYDOWN:
                    if e.key == py.K_r:
                        gamemain()  
                    else :
                        gameExit = True
                        gameover = False
        for e in py.event.get():
            if e.type == py.QUIT:
                gameExit=True
            if e.type == py.KEYDOWN:
                if e.key == py.K_LEFT or e.key == py.K_a:
                    cx=-20
                    cy=0
                if e.key == py.K_RIGHT or e.key == py.K_d:
                    cx=20
                    cy=0
                if e.key == py.K_UP or e.key == py.K_w:
                    cy=-20
                    cx=0
                if e.key == py.K_DOWN or e.key == py.K_s:
                    cy=20
                    cx=0
            if x>=disp_w or x<=0 or y>=disp_h or y<=0:
                gameover=True
        x+=cx
        y+=cy
        gameDisplay.fill(black)
        py.draw.rect(gameDisplay, blue,[x1,y1,20,20])
        xyelement=[]
        xyelement.append(x)
        xyelement.append(y)
        xandyelement.append(xyelement)
        if len(xandyelement) > basketlength:
            del xandyelement[0]
        for w in xandyelement[:-1]:
            if w == xyelement:
                gameover = True
        snake(xandyelement)
        score(count)
        py.display.update()
        if x == x1 and y == y1:
            x1 = round(random.randrange(0, disp_w - 20) / 20.0) * 20.0
            y1 = round(random.randrange(0, disp_h - 20) / 20.0) * 20.0
            basketlength+=1
            count+=1
            score(count)
            py.display.update()
            if(count%5==0):
                fps+=5
        clock.tick(fps)
    py.quit()
    quit()

def startscreen():
    tstartscreen()
    texit()
    py.display.update()
    gameend=False
    while not gameend:
       for e in py.event.get():
           if e.type == py.KEYDOWN:
               if e.key == py.K_1:
                   gamemain()
                   gameend=True
               if e.key == py.K_2:
                   gameend=True
                   exit()
startscreen()
