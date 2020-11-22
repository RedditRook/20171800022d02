from pico2d import *
from gobj import *
import gfw_image
from after import After
class Bomb:
    bombs = []
    def __init__(self, pos):
        imageName = '/bomb.png'
        self.image = gfw_image.load(RES_DIR + imageName)
        self.pos = pos
        self.delay=0
        self.count=0.01
    def draw(self):
        self.image.draw(*self.pos,50,50)
    def update(self):
        x,y = self.pos
        self.delay += self.count
        print(self.delay)
        if self.delay > 1:
            Bomb.bombs.remove(self)
            self.bombafter()

    def bombafter(self):
        after = After(self.pos)
        After.after.append(after)