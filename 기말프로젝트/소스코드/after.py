from pico2d import *
from gobj import *
import gfw_image

class After:
    after = []
    def __init__(self, pos):
        imageName = '/aftercenter.png'
        self.image = gfw_image.load(RES_DIR + imageName)
        self.pos = pos
        self.delay=0
        self.count=0.1
    def draw(self):
        self.image.draw(*self.pos,68,47)
    def update(self):
        x,y = self.pos
        self.delay += self.count
        if self.delay > 1:
            After.after.remove(self)