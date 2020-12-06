import gfw
import title_state
import winp1
from pico2d import *
import gfw_image
from gobj import *
from bomb import Bomb
from unwall import Unwall
import helper


class Player2:
    KEY_MAP = {
        (SDL_KEYDOWN, SDLK_LEFT):  (-1,  0),
        (SDL_KEYDOWN, SDLK_RIGHT): ( 1,  0),
        (SDL_KEYDOWN, SDLK_DOWN):  ( 0, -1),
        (SDL_KEYDOWN, SDLK_UP):    ( 0,  1),
        (SDL_KEYUP, SDLK_LEFT):    ( 1,  0),
        (SDL_KEYUP, SDLK_RIGHT):   (-1,  0),
        (SDL_KEYUP, SDLK_DOWN):    ( 0,  1),
        (SDL_KEYUP, SDLK_UP):      ( 0, -1),
    }
    KEYDOWN_ENTER = (SDL_KEYDOWN ,SDLK_KP_ENTER)
    KEYDOWN_R = (SDL_KEYDOWN,SDLK_r)
    image = None

    def __init__(self):        
        self.pos = 741,82
        self.save1= 0,0
        self.save2= 0,0
        self.save3= 0,0
        self.action = 3
        self.delta = 0, 0
        self.target = None
        self.targets = []
        self.speed = 0
        self.animation=0
        self.count=0.025
        self.lifecount=100

        if Player2.image == None:
            Player2.image = gfw_image.load(RES_DIR + '/player2.png')

    def draw(self):
        if(self.action == 3 or self.action==2 or self.action==6 or self.action ==7):# 가만히
                self.image.clip_draw(363,195,85,110,*self.pos)
        elif(self.action ==1):   #오른쪽
            if(self.animation <0.3):
                self.image.clip_draw(535,195,85,110,*self.pos)
            elif(self.animation >=0.3 and self.animation <0.6):
                self.image.clip_draw(625,195,85,110,*self.pos)
            elif(self.animation >=0.6 and self.animation <0.9):
                self.image.clip_draw(705,195,85,110,*self.pos)
        elif(self.action==0): #왼쪽
            if(self.animation <0.3):
                self.image.clip_draw(11,195,85,110,*self.pos)
            elif(self.animation >=0.3 and self.animation <0.6):
                self.image.clip_draw(97,195,85,110,*self.pos)
            elif(self.animation >=0.6 and self.animation <0.9):
                self.image.clip_draw(180,197,85,110,*self.pos)
        elif(self.action==4): #아래
            if(self.animation <0.3):
                self.image.clip_draw(363,195,85,110,*self.pos)
            elif(self.animation >=0.3 and self.animation <0.6):
                self.image.clip_draw(445,195,85,110,*self.pos)
            elif(self.animation >=0.6 and self.animation <0.9):
                self.image.clip_draw(283,195,85,110,*self.pos)
        elif(self.action==5): #위
            if(self.animation <0.3):
                self.image.clip_draw(450,305,85,110,*self.pos)
            elif(self.animation >=0.3 and self.animation <0.6):
                self.image.clip_draw(370,305,85,110,*self.pos)
            elif(self.animation >=0.6 and self.animation <0.9):
                self.image.clip_draw(286,305,85,110,*self.pos)

    def update(self):
        map1 = ((94,45),(94,135),(94,225),(94,320),(94,415),(94,508) ,\
                (230,45),(230,135),(230,225),(230,320),(230,415),(230,508) ,\
                (365,45),(365,135),(365,225),(365,320),(365,415),(365,508) ,\
                (503,45),(503,135),(503,225),(503,320),(503,415),(503,508) ,\
                (639,45),(639,135),(639,225),(639,320),(639,415),(639,508))

        x,y = self.pos
        dx,dy = self.delta
        self.pos = x+dx, y+dy
        self.animation +=self.count

        if(self.animation >0.9):
            self.animation =0
        if(x >741):
            self.pos=741,y+dy
        if(x <60):
            self.pos=60,y+dy
        if(y> 538):
            self.pos=x+dx,538
        if(y < 81):
            self.pos=x+dx,81
        

        sx1 , sy1 =self.save1
        if sx1 - 100 <= x and sx1 +100 >= x and sy1 -70 <= y and sy1 +70 >= y:
            self.lifecount -=0.1
        else:
            self.lifecount -=0.5
        sx2 , sy2 =self.save2
        if sx2 - 100 <= x and sx2 +100 >= x and sy2 -70 <= y and sy2 +70 >= y:
            self.lifecount -=0.1
        else:
            self.lifecount -=0.5

        sx3 , sy3 =self.save3
        if sx3 - 100 <= x and sx3 +100 >= x and sy3 -70 <= y and sy3 +70 >= y:
            self.lifecount -=0.1
        else:
            self.lifecount -=0.5

        if self.lifecount <0:
            gfw.change(winp1)

        for i in range(30):
            unx1 , uny1 =map1[i]
            if(self.action ==1 and(unx1 -20 < x and unx1 + 90 > x and uny1+20 < y and uny1 + 80 > y)):
                self.pos =x-5,y
            elif(self.action ==0 and(unx1-20 < x and unx1 + 90 > x and uny1+20 < y and uny1 + 80 > y)):
                self.pos =x+5,y
            elif(self.action ==5 and(unx1-20 < x and unx1 + 90 > x and uny1+20 < y and uny1 + 80 > y)):
                self.pos =x,y-5
            elif(self.action ==4 and(unx1-20 < x and unx1 + 90 > x and uny1+20 < y and uny1 + 80 > y)):
                self.pos =x,y+5

        if self.target is not None:
            ddx = -self.delta[0]
            helper.move_toward_obj(self)
            if self.target == None:
                del self.targets[0]
                if len(self.targets) > 0:
                    helper.set_target(self, self.targets[0])
                    self.updateAction(self.delta[0],0)
                else:
                    self.speed = 0
                    self.updateAction(0, ddx)

    def updateDelta(self, ddx, ddy):
        dx,dy = self.delta
        dx += ddx
        dy += ddy
        if ddx != 0:
            self.updateAction(dx, ddx)
        if ddy !=0:
            self.updateActionY(dy,ddy)
        self.delta = dx, dy

    def updateAction(self, dx, ddx):
        self.action = \
            0 if dx < 0 else \
            1 if dx > 0 else \
            2 if ddx > 0 else 3

    def updateActionY(self,dy,ddy):
        self.action = \
            4 if dy < 0 else \
            5 if dy >0 else \
            6 if ddy > 0 else 7

    def appendTarget(self, target):
        if target == self.pos: return
        for t in self.targets:
            if t == target: return

        self.targets.append(target)
        self.speed += 1
        helper.set_target(self, self.targets[0])
        self.updateAction(self.delta[0],0)

    def handle_event(self, e):
        pair = (e.type, e.key)
        if pair in Player2.KEY_MAP:
            if self.target is not None:
                if e.type == SDL_KEYUP: return
                self.updateAction(0, -self.delta[0])
                self.target = None
                self.delta = 0,0
                self.targets = []
                self.speed = 0
            self.updateDelta(*Player2.KEY_MAP[pair])
        elif pair == Player2.KEYDOWN_ENTER:
            self.fire()
        elif pair == Player2.KEYDOWN_R:
            gfw.change(title_state)


    def fire(self):
        if(len(Bomb.bombs)==0):
            self.save1=self.pos
            bomb = Bomb(self.save1)
        if(len(Bomb.bombs)==1):
            self.save2=self.pos
            bomb = Bomb(self.save2)
        if(len(Bomb.bombs)==2):
            self.save3=self.pos
            bomb = Bomb(self.save3)
        if(len(Bomb.bombs) < 3):
            Bomb.bombs.append(bomb)
            self.lifecount +=50