import random
from pico2d import *

RES_DIR = '../res'

class Field:
    def __init__(self):
        self.image = load_image(RES_DIR + '/playfieldtile.png')
        self.bgm=load_music(RES_DIR + '/stage.mp3')
        self.bgm.set_volume(16)
        self.bgm.repeat_play()
    def draw(self):
        self.image.draw(400, 300)
    def update(self):
        pass