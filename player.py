import pyglet
import math
from bullet import Bullet
from pyglet import shapes
from constants import Constants

class Player: 
    x_pos = 400
    y_pos = 400
    x_speed = Constants.X_MOVEMENT_SPEED
    y_speed = Constants.Y_MOVEMENT_SPEED
    rotation = 0
    batch = object

    player_img = pyglet.image.load("player.png")
    player_img.anchor_x = player_img.width // 2
    player_img.anchor_y = player_img.height

    player = pyglet.sprite.Sprite(player_img, x=x_pos, y=y_pos)

    def __init__(self, window, batch):
        self.player.update(scale=0.75)
        self.batch = batch
        self.player = pyglet.sprite.Sprite(self.player_img, x=self.x_pos, y=self.y_pos, batch=batch)

    def shoot(self):
        bullet = shapes.Circle(self.x_pos, self.y_pos, 3, color=(255, 255, 255), batch = self.batch)

    def calc_speed(self):
        angle = self.rotation % 90
        if angle == 0:
            if self.rotation == 0 or self.rotation == 180:
                self.x_speed = 0
                self.y_speed = Constants.Y_MOVEMENT_SPEED
            else:
                self.y_speed = 0
                self.x_speed = Constants.X_MOVEMENT_SPEED
        else:
            self.x_speed = abs(math.cos(angle)*5)
            self.y_speed = abs(math.sin(angle)*5)
        if self.rotation > 180:
            self.x_speed *= -1
        if self.rotation > 90 and self.rotation < 270:
            self.y_speed *= -1
        print("ROTATION: " + str(self.rotation) + " (" + str(angle) + "); X_SPEED: " + str(self.x_speed) + "; Y_SPEED: " + str(self.y_speed))

    def move(self, symbol, dt):
        if symbol == 119:
            self.calc_speed()
            self.y_pos += self.y_speed * dt
            self.x_pos += self.x_speed * dt
        if symbol == 97:
            self.rotation -= Constants.ROTATION_SPEED
            if self.rotation < 0:
                self.rotation = 360
        if symbol == 100:
            self.rotation += Constants.ROTATION_SPEED
            if self.rotation > 360:
                self.rotation = 0
        if symbol == 32:
            self.shoot()
        print(str(self.y_pos))
        self.player.update(x=self.x_pos, y=self.y_pos, rotation=self.rotation)
        self.player.draw()