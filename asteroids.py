import pyglet
from player import Player
from pyglet.window import key

window = pyglet.window.Window(800, 800, "Asteroids")
batch = pyglet.graphics.Batch()
#         W      A      D    SPACE
keys = [False, False, False, False]

player = Player(window, batch)

@window.event
def on_draw():
    window.clear()
    batch.draw()

@window.event
def on_key_press(symbol, modifiers):
    keys[0] = symbol == key.W
    keys[1] = symbol == key.A
    keys[2] = symbol == key.D
    keys[3] = symbol == key.SPACE
    print(keys[0])

def update(dt):
    if keys[0]:
        print("W")
        player.move(key.W, dt)
    if keys[1]:
        player.move(key.A, dt)
    if keys[2]:
        player.move(key.D, dt)
    if keys[3]:
        player.move(key.SPACE, dt)

pyglet.clock.schedule_interval(update, 0.01)

pyglet.app.run()