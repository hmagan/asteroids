import pyglet
import time
import random
import math
from constants import Constants
from bullet import Bullet
from player import Player
from pyglet.window import key
from pyglet import font
from rock import Rock
from animation import Animation

global game_started
game_started = False
global lives
lives = 3

window = pyglet.window.Window(Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT, "Asteroids")

icon = pyglet.image.load("res/icon.png")
font.add_file("res/hyperspace.ttf")
hyperspace = font.load("Hyperspace", 16)

window.set_icon(icon, icon)
main_batch = pyglet.graphics.Batch()
#         W      A      D
keys = [False, False, False]

player = Player(window, main_batch)
bullets = []
bullet_times = []
particles = []
particles_times = []
asteroids = []

lives_label = pyglet.text.Label(
    "Lives: " + str(lives),
    font_name="Hyperspace",
    font_size=25, 
    x=125, y=Constants.WINDOW_HEIGHT - 50, 
    anchor_x="center", anchor_y="center", 
    batch=main_batch)

def collided(obj1, obj2):
    return abs(math.sqrt((obj1.get_x() - obj2.get_x()) ** 2 + (obj1.get_y() - obj2.get_y()) ** 2) - obj1.get_radius() - obj2.get_radius()) <= 5

def explode(x, y, pl):
    global lives
    particles.extend([
        Animation(x, y, random.randint(0, 360)), 
        Animation(x, y, random.randint(0, 360)), 
        Animation(x, y, random.randint(0, 360)), 
        Animation(x, y, random.randint(0, 360)), 
        Animation(x, y, random.randint(0, 360)), 
        Animation(x, y, random.randint(0, 360)), 
        Animation(x, y, random.randint(0, 360)), 
        Animation(x, y, random.randint(0, 360))
    ])
    particles_times.extend([0, 0, 0, 0, 0, 0, 0, 0])
    if pl:
        lives -= 1
        lives_label.text = "Lives: " + str(lives)
        player.x_pos = 999
        player.y_pos = 999

@window.event
def on_key_press(symbol, modifiers):
    global game_started
    global lives
    if not game_started:
        if symbol == key.ENTER:
            game_started = True
        else: 
            return
    if lives > 0:
        if symbol == key.W:
            player.thrust = True
            player.toggle_sprite()
            keys[0] = True
        if symbol == key.A:
            keys[1] = True
        if symbol == key.D:
            keys[2] = True
        if symbol == key.SPACE:
            bullets.append(Bullet(player.x_pos, player.y_pos, player.rotation))
            bullet_times.append(0)
        if symbol == key.R:
            asteroids.append(
                Rock(
                    random.choice([random.randint(0, Constants.WINDOW_WIDTH//2-200), random.randint(Constants.WINDOW_WIDTH//2+200, Constants.WINDOW_WIDTH)]),
                    random.choice([random.randint(0, Constants.WINDOW_HEIGHT//2-200), random.randint(Constants.WINDOW_HEIGHT//2+200, Constants.WINDOW_HEIGHT)]), 
                    3, 
                    random.choice([random.randint(-250, -30), random.randint(30, 250)]))
            )

@window.event
def on_key_release(symbol, modifiers):
    if not game_started:
        return
    if symbol == key.W:
        player.thrust = False
        player.toggle_sprite()
        keys[0] = False
    if symbol == key.A:
        keys[1] = False
    if symbol == key.D:
        keys[2] = False

global hidden
hidden = True
global t
t = time.time()

def update(dt):
    global hidden
    global t
    if not game_started:
        if time.time() - t > 1: # 1 second
            t = time.time()
            if hidden:
                hidden = False
            else:
                hidden = True
        return
    player.move(dt, keys)
    for bullet in bullets:
        bullet.move(dt)
    i = 0
    while i < len(asteroids):
        asteroids[i].move(dt)
        if collided(player, asteroids[i]):  
            explode(player.x_pos, player.y_pos, True)
        else:
            j = 0
            while j < len(bullets):
                if collided(asteroids[i], bullets[j]):
                    if asteroids[i].level > 1:
                        asteroids.append(
                            Rock(
                                asteroids[i].x - 50,
                                asteroids[i].y, 
                                asteroids[i].level-1, 
                                random.choice([random.randint(-250, -30), random.randint(30, 250)]))
                        )
                        asteroids.append(
                            Rock(
                                asteroids[i].x + 50,
                                asteroids[i].y, 
                                asteroids[i].level-1, 
                                random.choice([random.randint(-250, -30), random.randint(30, 250)]))
                        )
                    explode(asteroids[i].x, asteroids[i].y, False)
                    asteroids.pop(i)
                    i -= 1
                    bullets.pop(j)
                    bullet_times.pop(j)
                    break
                j += 1
        i += 1
    for particle in particles:
        particle.move(dt)

pyglet.clock.schedule_interval(update, 1/60.0) # update at 60Hz

title = pyglet.text.Label(
        "Asteroids 1979",
        font_name="Hyperspace",
        font_size=65, 
        x=Constants.WINDOW_WIDTH//2, y=Constants.WINDOW_HEIGHT//2+50, 
        anchor_x="center", anchor_y="center")
subheading = pyglet.text.Label(
        "in Python!",
        font_name="Hyperspace",
        font_size=30,
        x=Constants.WINDOW_WIDTH//2, y=Constants.WINDOW_HEIGHT//2-50,
        anchor_x="center", anchor_y="center")
push_enter = pyglet.text.Label(
        "PUSH ENTER",
        font_name="Hyperspace",
        font_size=40,
        x=Constants.WINDOW_WIDTH//2, y=Constants.WINDOW_HEIGHT//2-150,
        anchor_x="center", anchor_y="center")

@window.event
def on_draw():
    global game_ended
    window.clear()
    if game_started:
        if lives <= 0:
            print("GABE")
        else:
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
        i = 0
        while i < len(particles):
            if particles_times[i] > Constants.PARTICLE_LIFETIME: 
                particles.pop(i)
                particles_times.pop(i)
            else: 
                particles[i].draw()
                particles_times[i] += 1
                i += 1
        for asteroid in asteroids:
            asteroid.draw()
    else:
        title.draw()
        subheading.draw()
        if not hidden:
            push_enter.draw()

pyglet.app.run()