import pyglet
import random
import math
from constants import Constants

class Rock:
    level = 3
    x = 0
    y = 0
    dir = 0
    rot = 0
    r = 0
    x_speed = 0
    y_speed = 0
    asteroid_img = random.choice(Constants.LARGE_ASTEROID_SPRITES)
    asteroid_img.anchor_x = asteroid_img.width // 2
    asteroid_img.anchor_y = asteroid_img.height // 2
    asteroid = pyglet.sprite.Sprite(asteroid_img, x=400, y=400)

    def __init__(self, x, y, level, dir):
        self.level = level
        self.dir = dir
        self.x = x
        self.y = y
        if level == 3:
            self.asteroid_img = random.choice(Constants.LARGE_ASTEROID_SPRITES)
            self.r = 48
        elif level == 2:
            self.asteroid_img = random.choice(Constants.MEDIUM_ASTEROID_SPRITES)
            self.r = 24
        elif level == 1: 
            self.asteroid_img = random.choice(Constants.SMALL_ASTEROID_SPRITES)
            self.r = 12

        if self.dir == 0 or self.dir == 360:
            self.y_speed = random.randint(Constants.MIN_ASTEROID_SPEED, Constants.MAX_ASTEROID_SPEED)
            self.x_speed = 0
        elif self.dir == 90:
            self.x_speed = random.randint(Constants.MIN_ASTEROID_SPEED, Constants.MAX_ASTEROID_SPEED)
            self.y_speed = 0
        elif self.dir == 180:
            self.y_speed = -random.randint(Constants.MIN_ASTEROID_SPEED, Constants.MAX_ASTEROID_SPEED)
            self.x_speed = 0
        elif self.dir == 270:
            self.x_speed = -random.randint(Constants.MIN_ASTEROID_SPEED, Constants.MAX_ASTEROID_SPEED)
            self.y_speed = 0
        else: 
            hyp = random.randint(Constants.MIN_ASTEROID_SPEED, Constants.MAX_ASTEROID_SPEED)
            angle = self.dir % 90
            x_diff = abs(math.cos(math.radians(angle)) * hyp)
            y_diff = abs(math.sin(math.radians(angle)) * hyp)
            if self.dir > 180:
                if self.dir < 270:
                    x_diff = abs(math.sin(math.radians(angle)) * hyp)
                    y_diff = abs(math.cos(math.radians(angle)) * hyp)
                self.x_speed -= x_diff
            else:
                if self.dir < 90:
                    x_diff = abs(math.sin(math.radians(angle)) * hyp)
                    y_diff = abs(math.cos(math.radians(angle)) * hyp)
                self.x_speed += x_diff
            if self.dir > 90 and self.dir < 270:
                self.y_speed -= y_diff
            else:
                self.y_speed += y_diff

        self.asteroid_img.anchor_x = self.asteroid_img.width // 2
        self.asteroid_img.anchor_y = self.asteroid_img.height // 2
        self.asteroid = pyglet.sprite.Sprite(self.asteroid_img, x=x, y=y)

    def draw(self):
        self.asteroid.draw()

    def check_for_offscreen(self):
        if self.x < 0:
            self.x = Constants.WINDOW_WIDTH
        if self.x > Constants.WINDOW_WIDTH:
            self.x = 0
        if self.y < 0:
            self.y = Constants.WINDOW_HEIGHT
        if self.y > Constants.WINDOW_HEIGHT:
            self.y = 0

    def move(self, dt):
        self.x += self.x_speed * dt
        self.y += self.y_speed * dt
        self.rot += self.dir * dt
        if self.rot < 0:
            self.rot = 360 - abs(self.rot)
        if self.rot > 360:
            self.rot = self.rot - 360
        self.check_for_offscreen()
        self.asteroid.update(x=self.x, y=self.y, rotation=self.rot)
    
    # OOP
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
        
    def get_radius(self):
        return self.r