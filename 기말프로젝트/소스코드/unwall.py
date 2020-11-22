from pico2d import *
from gobj import *
import gfw_image

class Unwall:
    unwall = []
    def __init__(stage):
        stage =0

    def draw(stage):
        imageName = '/wall.png'
        image = gfw_image.load(RES_DIR + imageName)
        if(stage ==1):
            image.draw(400,300,50,50)
            image.draw(150,300,50,50)
            image.draw(200,100,50,50)
            image.draw(700,150,50,50)