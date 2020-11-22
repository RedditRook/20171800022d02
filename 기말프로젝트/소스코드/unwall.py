from pico2d import *
from gobj import *
import gfw_image

class Unwall:
    unwall = []
    def __init__(stage):
        stage =0
    def draw(stage):
        #x증가 68  y 증가 45 
        pos1 = ((26,45),(94,90),(162,135),(230,180))
        pos2 = ((26,45),(94,90),(162,135),(230,180)) 
        imageName = '/wall.png'
        image = gfw_image.load(RES_DIR + imageName)
        if(stage ==1):  # 가로 68 세로 47 #필드 좌하단 26,45 검정 줄 5 
            image.draw_to_origin(*pos1[0],68,47)
            image.draw_to_origin(*pos1[1],68,47)
            image.draw_to_origin(*pos1[2],68,47)
            image.draw_to_origin(*pos1[3],68,47)
        elif(stage==2):
            image.draw_to_origin(*pos[0],68,47)
            image.draw_to_origin(*pos[1],68,47)
            image.draw_to_origin(*pos[2],68,47)
            image.draw_to_origin(*pos[3],68,47)