import random
from pico2d import *
import gfw_image
from gobj import *
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

    def __init__(self, rand_pos=False):
        self.pos = 55,510
        self.action = 3
        self.delta = 0, 0
        self.fidx = random.randint(0, 7)
        self.target = None
        self.targets = []
        self.speed = 0
        if Player.image == None:
            Player.image = gfw_image.load(RES_DIR + '/player.png')

    def draw(self):
        self.image.clip_draw(366, 191, 80, 110 , *self.pos,60,90)
        
    def update(self):
        x,y = self.pos
        dx,dy = self.delta
        self.pos = x+dx, y+dy

        if self.target is not None:
            ddx = -self.delta[0]
            helper.move_toward_obj(self)
            if self.target == None:
                print("Removing target: ", self.targets[0], " from %d target(s)." % len(self.targets))
                del self.targets[0]
                if len(self.targets) > 0:
                    helper.set_target(self, self.targets[0])
                    self.updateAction(self.delta[0],0)
                else:
                    self.speed = 0
                    self.updateAction(0, ddx)
        self.fidx = (self.fidx + 1) % 8

    def updateDelta(self, ddx, ddy):
        dx,dy = self.delta
        dx += ddx
        dy += ddy
        if ddx != 0:
            self.updateAction(dx, ddx)
        self.delta = dx, dy

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