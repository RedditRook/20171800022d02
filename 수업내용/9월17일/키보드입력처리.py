from pico2d import *
os.chdir('C:\\Users\\user\\Desktop\\대학\\2d게임프로그래밍\\resource')

def handle_events():
    global running,dx
    events = get_events()
    for event in events:
        if event.type ==SDL_QUIT:
            running =False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dx +=1
            elif event.key ==SDLK_LEFT:
                dx -=1
            elif event.key ==SDLK_ESCAPE:
                runnning =False
        elif event.type ==SDL_KEYUP:
            if event.key ==SDLK_RIGHT:
                dx -=1
            elif event.key ==SDLK_LEFT:
                dx +=1

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

running =True
x=get_canvas_width()//2
dx=0
while running:
    clear_canvas()
    grass.draw(400,30)
    character.draw(x,90)
    update_canvas()
    handle_events()
    x +=dx

close_canvas()