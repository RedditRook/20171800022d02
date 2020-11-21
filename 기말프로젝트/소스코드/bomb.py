from pico2d import *
from gobj import *
import gfw_image

class Bomb:
    bombs = []
    def __init__(self, pos, delta):
        imageName = '/bomb.png'
        self.image = gfw_image.load(RES_DIR + imageName)
        self.pos = pos
        self.delta = delta
        self.radius = self.image.h // 2
    def draw(self):
        self.image.draw(*self.pos,50,50)
    def update(self):
        x,y = self.pos
        count=0
        delay=0.01
        
        count = count +delay

        if count == 1:
            Bomb.bombs.remove(self)