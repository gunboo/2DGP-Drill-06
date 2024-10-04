from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
mouse = load_image('hand_arrow.png')

def random_location():
    global target_x, target_y
    target_x, target_y = random.randint(100, 1200), random.randint(100, 950)

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

running = True
frame = 0
hide_cursor()
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
target_x, target_y = x, y
direction = 1
speed = 10


random_location()

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)


    mouse.draw(target_x, TUK_HEIGHT - target_y)


    if x < target_x:
        direction = -1
    elif x > target_x:
        direction = 1


    character.clip_draw(frame * 100, (1 if direction == -1 else 0) * 100, 100, 100, x, y)

    update_canvas()
    handle_events()


    if abs(x - target_x) < 5 and abs(y - (TUK_HEIGHT - target_y)) < 5:
        random_location()


    if x < target_x:
        x += min(speed, target_x - x)
    elif x > target_x:
        x -= min(speed, x - target_x)

    if y < (TUK_HEIGHT - target_y):
        y += min(speed, (TUK_HEIGHT - target_y) - y)
    elif y > (TUK_HEIGHT - target_y):
        y -= min(speed, y - (TUK_HEIGHT - target_y))

    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()