import pyglet
import math
import random
from pyglet import shapes
from constants import Constants

class Animation:
    x = 0
    y = 0
    x_speed = 0
    y_speed = 0
    dir = 0
    obj = shapes.Circle(0, 0, 0, color=(255, 255, 255))

    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir

        speed = random.randint(Constants.MIN_PARTICLE_SPEED, Constants.MAX_PARTICLE_SPEED)
        if self.dir == 0 or self.dir == 360:
            self.y_speed = speed
            self.x_speed = 0
        elif self.dir == 90:
            self.x_speed = speed
            self.y_speed = 0
        elif self.dir == 180:
            self.y_speed = -speed
            self.x_speed = 0
        elif self.dir == 270:
            self.x_speed = -speed
            self.y_speed = 0
        else: 
            hyp = speed
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

        self.obj = shapes.Circle(x, y, 1, color=(0, 0, 0))

    def draw(self):
        self.obj.draw()

    def move(self, dt):
        self.x += self.x_speed * dt
        self.y += self.y_speed * dt
        self.obj = pyglet.shapes.Circle(self.x, self.y, 1, color=(255, 255, 255))