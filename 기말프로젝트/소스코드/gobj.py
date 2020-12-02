import random
from pico2d import *

RES_DIR = '../res'

class Field:
    def __init__(self):
        self.image = load_image(RES_DIR + '/playfieldtile.png')
    def draw(self):
        self.image.draw(400, 300)
    def update(self):
        pass