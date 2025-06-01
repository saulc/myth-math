'''
Created on Oct 2, 2015

@author: saul
'''
import pygame

class Ring:
    start = 88
    sw = 1000

    def __init__(self , x, y, st=0, c = 0):
        self.x = x
        self.y = y
        self.xsize = Ring.start
        self.ysize = Ring.start
        if c >= len(Circles.colors): c = 0
        self.cc = c
        self.color = Circles.c2[self.cc]
        self.a = st
        self.vx = 0
        self.vy = 0

    def draw(self, screen): 
        pygame.draw.ellipse(screen, self.color, [self.x, self.y, self.xsize, self.ysize], 1)

        # pygame.draw.ellipse(screen, self.color, [self.sw/2 + self.x/2, self.y, self.xsize, self.ysize], 1)
        
        # pygame.draw.ellipse(screen, self.color, [self.sw/2 - self.x/2, self.y, self.xsize, self.ysize], 1)
      # pygame.draw.rect(screen, self.color, [self.x, self.y, self.xsize, self.ysize], 1)

    def update(self):
        self.color = Circles.c2[self.cc]
        self.xsize += self.a
        self.ysize += self.a
        self.x -= self.a//2
        self.y -= self.a//2
        if self.xsize <= 1: self.xsize = 11
        if self.ysize <= 1: self.ysize = 11
        # self.x += -self.vx
        # self.y += self.vy


class Circles:
    #class variables
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 5, 5)
    im = (255, 155, 0)
    green = (0, 188, 0)
    gg = (0, 188, 88)
    pink = (200, 0, 100)
    orange = (255, 115, 90)
    colors = [black, white, red, im, green, gg, pink]
    c2 = [  orange, gg, red, im, green, pink]
    sw = 1000
    maxspeed = 5
    upspeed = 3
    bg = 0
    circle = []
    firstloop = True

    def __init__(self ,  c = 11):
        self.cc = c
        self.ct = 111
        self.vx = 0
        self.vy = 0
        self.x = Circles.sw//2 - Ring.start//2
        self.y = Circles.sw//2 - Ring.start//2
        self.a = Circles.maxspeed
        if Circles.firstloop:
            self.startGame()
            Circles.firstloop = False

    def startGame(self):

        pygame.init()
        screensize = [Circles.sw, Circles.sw]
        screen = pygame.display.set_mode(screensize)
        pygame.display.set_caption('green')
        done = False
        clock = pygame.time.Clock()
        Circles.circle.append(Ring(Circles.sw//2, Circles.sw//2, 3, 1))
        t = 0
        while not done:
            self.checkKb()
        #    circlez = Circles() #x, y, start, start, colors[cc])
            screen.fill(Circles.colors[Circles.bg])
            # circlez.x += x
            # circlez.y += y
            # print( ' #: ' + str(len( Circles.circle)))
            self.printInfo()
            self.update()
            for c in Circles.circle:
                c.draw(screen)
                c.update()

            pygame.display.flip()
            clock.tick(60)
            self.addc()

            t += 1
            if t > self.ct:
                t = 0
                self.cc+=1
                if self.cc >= len(Circles.c2): self.cc = 0

        pygame.quit()
        # loop this . . .

    def addc(self):
        # for i in range(3):
            Circles.circle.append(Ring(self.x, self.y, 3, self.cc))


    def checkBounds(self):
        if self.x > Circles.sw -Ring.start or self.x < 0: self.vx *= -1
        if self.y > Circles.sw -Ring.start or self.y < 0: self.vy *= -1


    def printInfo(self):
        print( 'vx: ' + str(self.vx) + ' vy: ' + str(self.vy) +' pos: ' + str(len(Circles.circle) ) +' a: ' + str(self.a) )

    def update(self):
        self.checkBounds()
        self.x -= self.vx
        self.y += self.vy
        for r in Circles.circle:
            r.color = Circles.c2[r.cc]
            r.a = self.a
            # rx += self.
            # r.x = self.x - r.xsize//2
            # r.y = self.y - r.ysize//2
            r.vx = self.vx
            r.vy = self.vy
            r.cc = self.cc
            if r.xsize >= Circles.sw/2 or r.ysize >= Circles.sw/2 or r.xsize <=2:
                Circles.circle.remove(r)
                print('Circle removed')

    def remove(self):
        Circles.circle.remove(self)
        del self

    def checkKb(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                print('time to quit')
                pygame.quit()
                break

            if event.type == pygame.KEYDOWN:
                print(' --Key pressed ' + str(event.key))
                if event.key == pygame.K_RIGHT:
                    self.vx += -Circles.maxspeed
                if event.key == pygame.K_LEFT:
                    self.vx += Circles.maxspeed
                if event.key == pygame.K_DOWN:
                    self.vy += Circles.maxspeed
                if event.key == pygame.K_UP:
                    self.vy += -Circles.maxspeed

            if event.type == pygame.KEYUP:
                print(' --Key released ' + str(event.key))
                if event.key == pygame.K_RIGHT:
                    self.vx = -Circles.upspeed
                if event.key == pygame.K_LEFT:
                    self.vx = Circles.upspeed
                if event.key == pygame.K_DOWN:
                    self.vy = Circles.upspeed
                if event.key == pygame.K_UP:
                    self.vy = -Circles.upspeed
                if event.key == pygame.K_ESCAPE:
                    print('time to quit')
                    pygame.quit()
                    break
                    done = True
                if event.key == pygame.K_q:
                    self.addc()
                if event.key == pygame.K_x:
                    self.vx += 10
                if event.key == pygame.K_c:
                    self.vx += -10
                if event.key == pygame.K_a:
                    self.vy += 1
                if event.key == pygame.K_z:
                    self.vy += -1
                if event.key == pygame.K_s:
                    self.a += 1
                if event.key == pygame.K_d:
                    self.a -= 1
                    # if self.a < 0 : self.a = 0
                if event.key == pygame.K_b:
                    Circles.bg += 1
                    if Circles.bg >= len(Circles.colors): Circles.bg = 0
                if event.key == pygame.K_v:
                    self.cc += 1
                    if self.cc >= len(Circles.c2): self.cc = 0
                if event.key == pygame.K_n:
                    self.ct += 33
                if event.key == pygame.K_m:
                    self.ct -= 33


if __name__ == '__main__':
    Circles(3)
