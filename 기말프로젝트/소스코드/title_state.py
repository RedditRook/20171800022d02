import gfw
from pico2d import *
import game_state

RES_DIR = './res'

def enter():
    global image,sound
    image = load_image(RES_DIR + '/title.png')
    sound = load_music(RES_DIR + '/title.mp3')
    sound.set_volume(64)
    sound.repeat_play()

def update():
    pass

def draw():
    image.draw(400, 300)

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
        gfw.push(game_state)
def exit():
    global image
    del image

def pause():
    pass
def resume():
    pass
    
if __name__ == '__main__':
    gfw.run_main()