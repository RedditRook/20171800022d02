import random
from pico2d import *
import gfw_image
from gobj import *
from bomb import Bomb
import helper

class Player:
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
    KEYDOWN_SPACE = (SDL_KEYDOWN, SDLK_SPACE)
    image = None

    def __init__(self):        
        self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.action = 3
        self.delta = 0, 0
        self.target = None
        self.targets = []
        self.speed = 0
        self.animation=0
        self.count=0.025
        if Player.image == None:
            Player.image = gfw_image.load(RES_DIR + '/player.png')

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
        stage1 = ((26,45),(94,90),(162,135),(230,180))
        
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

        unx1 , uny1 =stage1[3]
        if(unx1 <= x and unx1 + 63 >= x and uny1+20 <= y and uny1 + 80 >= y):
            print(unx1,uny1 ,"충돌",x,y)
        

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
        if pair in Player.KEY_MAP:
            if self.target is not None:
                if e.type == SDL_KEYUP: return
                self.updateAction(0, -self.delta[0])
                self.target = None
                self.delta = 0,0
                self.targets = []
                self.speed = 0
            self.updateDelta(*Player.KEY_MAP[pair])
        elif pair == Player.KEYDOWN_SPACE:
            self.fire()

    def fire(self):
        bomb = Bomb(self.pos)
        if(len(Bomb.bombs) < 3):
            Bomb.bombs.append(bomb)
        print('Bomb count = %d' % len(Bomb.bombs))