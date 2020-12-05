import gfw
from pico2d import *
from gobj import *
from player import Player
from player2 import Player2
from bomb import Bomb
from after import After
from unwall import Unwall
from canwall import Canwall

def enter():
    global field, player,player2
    field = Field()
    player = Player()
    player2 = Player2()

def update():
    player.update()
    player2.update()
    for b in Bomb.bombs: b.update()
    for a in After.after: a.update()

def draw():
    field.draw()
    Unwall.draw()
    for b in Bomb.bombs: b.draw()
    for a in After.after: a.draw()
    player.draw()
    player2.draw()

def handle_event(e):
    global player,player2
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

    player.handle_event(e)
    player2.handle_event(e)

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()