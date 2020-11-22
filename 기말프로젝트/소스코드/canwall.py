from pico2d import *
from gobj import *
import gfw_image

class Canwall:
    canwall = []
    def __init__(stage):
        stage =0

    def draw(stage):
        imageName = '/break.png'
        image = gfw_image.load(RES_DIR + imageName)
        if(stage ==1):  # 가로 68 세로 47
            image.draw_to_origin(200,300,68,47)