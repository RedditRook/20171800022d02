import gfw
from pico2d import *
from gobj import *
from player import Player
from bomb import Bomb

def enter():
    global field, player
    field = Field()
    player = Player()

def update():
    player.update()
    for b in Bomb.bombs: b.update()

def draw():
    field.draw()
    for b in Bomb.bombs: b.draw()
    player.draw()

def handle_event(e):
    global player
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

    player.handle_event(e)

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()