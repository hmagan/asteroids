import pyglet
import math
from pyglet import shapes
from constants import Constants

class Bullet:
    x = 0
    y = 0
    dir = 0
    r = 1

    x_speed = 0
    y_speed = 0

    bullet = pyglet.shapes.Circle(400, 400, r, color=(0, 0, 0))

    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir

        if self.dir == 0 or self.dir == 360:
            self.y_speed = Constants.BULLET_SPEED
            self.x_speed = 0
        elif self.dir == 90:
            self.x_speed = Constants.BULLET_SPEED
            self.y_speed = 0
        elif self.dir == 180:
            self.y_speed = -Constants.BULLET_SPEED
            self.x_speed = 0
        elif self.dir == 270:
            self.x_speed = -Constants.BULLET_SPEED
            self.y_speed = 0
        else: 
            hyp = Constants.BULLET_SPEED
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
        self.bullet = pyglet.shapes.Circle(x, y, self.r, color=(255, 255, 255))

    def draw(self):
        self.bullet.draw()

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
        self.check_for_offscreen()
        self.bullet = pyglet.shapes.Circle(self.x, self.y, self.r, color=(255, 255, 255))

    # OOP
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
        
    def get_radius(self):
        return self.r