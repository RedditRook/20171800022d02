from pico2d import *
from gobj import *
import gfw_image
from after import After

class Bomb:
    bombs = []
    def __init__(self , pos):
        imageName = '/bomb.png'
        self.image = gfw_image.load(RES_DIR + imageName)
        x ,y =pos
        self.pos = x , y - 10
        self.delay=0
        self.count=0.005

        self.sound1=load_wav(RES_DIR + '/a.wav')
        self.sound1.set_volume(16)
        self.sound2=load_wav(RES_DIR + '/b.wav')
        self.sound2.set_volume(64)
    def draw(self):
        self.image.draw(*self.pos,50,50)
    def update(self):
        x,y = self.pos
        self.delay += self.count
        self.sound1.play()
        if self.delay > 1:
            self.sound2.play()
            Bomb.bombs.remove(self)
            self.bombafter()

    def bombafter(self):
        after = After(self.pos)
        After.after.append(after)