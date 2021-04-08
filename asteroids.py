import pyglet
from pyglet.window import key
from player import Player

window = pyglet.window.Window(800, 800)
keys = key.KeyStateHandler()
window.push_handlers(keys)

player = Player()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.W or symbol == key.A or symbol == key.S or symbol == key.D:
        player.move(symbol)

@window.event
def on_draw():
    window.clear()
    player.draw()

pyglet.app.run()