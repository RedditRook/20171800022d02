from pico2d import *
from gobj import *
import gfw_image

class Unwall:
    unwall = []
    def __init__(map):
        map =0
    def draw(map):
        #x증가 68  y 증가 45 
        pos1 = ((94,45),(94,135),(94,225),(94,320),(94,415),(94,508) ,\
                (230,45),(230,135),(230,225),(230,320),(230,415),(230,508) ,\
                (365,45),(365,135),(365,225),(365,320),(365,415),(365,508) ,\
                (503,45),(503,135),(503,225),(503,320),(503,415),(503,508) ,\
                (639,45),(639,135),(639,225),(639,320),(639,415),(639,508))
        imageName = '/wall.png'
        image = gfw_image.load(RES_DIR + imageName)
        if(map ==1):  # 가로 68 세로 47 #필드 좌하단 26,45 검정 줄 5 
            for i in range(30):
                image.draw_to_origin(*pos1[i],68,47)
        