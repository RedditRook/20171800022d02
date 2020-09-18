from pico2d import *
os.chdir('C:\\Users\\user\\Desktop\\대학\\2d게임프로그래밍\\resource')

width = 1280
height = 1024

def handle_events():
    global running,x,y
    events =get_events()
    for event in events:
        if event.type ==SDL_QUIT:
            runnig =False
        elif event.type ==SDL_MOUSEMOTION:
            x,y=event.x, height -1 - event.y
        elif event.type ==SDL_KEYDOWN and event.key ==SDLK_ESCAPE:
            running =False

open_canvas(width,height)

grass = load_image('grass.png')
character = load_image('character.png')

running =True
x=get_canvas_width()//2
dx=0
while running:
    clear_canvas()
    grass.draw(400,30)
    grass.draw (800,30)
    character.draw(x,90)
    update_canvas()
    handle_events()
    x +=dx

close_canvas()