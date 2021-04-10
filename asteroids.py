import pyglet
from constants import Constants
from bullet import Bullet
from player import Player
from pyglet.window import key

window = pyglet.window.Window(Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT, "Asteroids")
main_batch = pyglet.graphics.Batch()
#         W      A      D
keys = [False, False, False]

player = Player(window, main_batch)
bullets = []
bullet_times = []

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.W:
        keys[0] = True
    if symbol == key.A:
        keys[1] = True
    if symbol == key.D:
        keys[2] = True
    if symbol == key.SPACE:
        bullets.append(Bullet(player.x_pos, player.y_pos, player.rotation))
        bullet_times.append(0)

@window.event
def on_key_release(symbol, modifiers):
    if symbol == key.W:
        keys[0] = False
    if symbol == key.A:
        keys[1] = False
    if symbol == key.D:
        keys[2] = False

def update(dt):
    player.move(dt, keys)
    for bullet in bullets:
        bullet.move(dt)

pyglet.clock.schedule_interval(update, 1/60.0) # update at 60Hz

@window.event
def on_draw():
    window.clear()
    main_batch.draw()
    i = 0
    while i < len(bullets):
        if bullet_times[i] > Constants.BULLET_LIFETIME: 
            bullets.pop(i)
            bullet_times.pop(i)
        else: 
            bullets[i].draw()
            bullet_times[i] += 1
            i += 1

pyglet.app.run()