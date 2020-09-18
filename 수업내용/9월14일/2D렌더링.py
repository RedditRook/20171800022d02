from pico2d import *
os.chdir('C:\\Users\\user\\Desktop\\대학\\2d게임프로그래밍\\resource')

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x=0
while (x<800):
    clear_canvas()
    grass.draw_now(400,30)
    character.draw_now(x,90)
    x +=2
    delay(0.01)

close_canvas()