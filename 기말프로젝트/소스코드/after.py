from pico2d import *
from gobj import *
import gfw_image

class After:
    after = []
    def __init__(self, pos):
        imageName = '/aftercenter.png'
        imageName1 = '/aftersider.png'
        imageName2 = '/aftersidel.png'
        imageName3 = '/aftersideu.png'
        imageName4 = '/aftersided.png'
        self.image = gfw_image.load(RES_DIR + imageName)
        self.image1 = gfw_image.load(RES_DIR + imageName1)
        self.image2 = gfw_image.load(RES_DIR + imageName2)
        self.image3 = gfw_image.load(RES_DIR + imageName3)
        self.image4 = gfw_image.load(RES_DIR + imageName4)
        self.pos = pos
        self.delay=0
        self.count=0.1
    def draw(self):
        x , y =self.pos
        self.image.draw(*self.pos,68,47)
        self.image1.draw(x+68,y,68,47)
        self.image2.draw(x-68,y,68,47)
        self.image3.draw(x,y+47,68,47)
        self.image4.draw(x,y-47,68,47)
    def update(self):
        x,y = self.pos
        self.delay += self.count
        if self.delay > 1:
            After.after.remove(self)