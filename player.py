import pyglet
import math
from pyglet import shapes
from constants import Constants

class Player: 
    x_pos = Constants.WINDOW_WIDTH // 2
    y_pos = Constants.WINDOW_HEIGHT // 2
    x_speed = 0
    y_speed = 0
    rotation = 0
    batch = object
    thrust = False

    player_img = pyglet.image.load("res/player.png")
    player_img.anchor_x = player_img.width // 2
    player_img.anchor_y = player_img.height // 2

    player_thrust_img = pyglet.image.load("res/player_thrust.png")
    player_thrust_img.anchor_x = player_thrust_img.width // 2
    player_thrust_img.anchor_y = player_thrust_img.height // 2

    player = pyglet.sprite.Sprite(player_img, x=x_pos, y=y_pos)

    def __init__(self, window, batch):
        self.batch = batch
        self.player = pyglet.sprite.Sprite(self.player_img, x=self.x_pos, y=self.y_pos, batch=batch)
        
    def toggle_sprite(self):
        if self.thrust:
            self.player = pyglet.sprite.Sprite(self.player_thrust_img, x=self.x_pos, y=self.y_pos, batch=self.batch)
        else:
            self.player = pyglet.sprite.Sprite(self.player_img, x=self.x_pos, y=self.y_pos, batch=self.batch)
        self.player.update(rotation=self.rotation)

    def calc_speed(self):
        if self.rotation == 0 or self.rotation == 360:
            self.y_speed += Constants.MOVEMENT_SPEED
        elif self.rotation == 90:
            self.x_speed += Constants.MOVEMENT_SPEED
        elif self.rotation == 180:
            self.y_speed -= Constants.MOVEMENT_SPEED
        elif self.rotation == 270:
            self.x_speed -= Constants.MOVEMENT_SPEED
        else: 
            hyp = Constants.MOVEMENT_SPEED
            angle = self.rotation % 90
            x = abs(math.cos(math.radians(angle)) * hyp)
            y = abs(math.sin(math.radians(angle)) * hyp)
            if self.rotation > 180:
                if self.rotation < 270:
                    x = abs(math.sin(math.radians(angle)) * hyp)
                    y = abs(math.cos(math.radians(angle)) * hyp)
                self.x_speed -= x
            else:
                if self.rotation < 90:
                    x = abs(math.sin(math.radians(angle)) * hyp)
                    y = abs(math.cos(math.radians(angle)) * hyp)
                self.x_speed += x
            if self.rotation > 90 and self.rotation < 270:
                self.y_speed -= y
            else:
                self.y_speed += y
        if self.x_speed < -Constants.MAX_SPEED:
            self.x_speed = -Constants.MAX_SPEED
        if self.x_speed > Constants.MAX_SPEED:
            self.x_speed = Constants.MAX_SPEED
        if self.y_speed < -Constants.MAX_SPEED:
            self.y_speed = -Constants.MAX_SPEED
        if self.y_speed > Constants.MAX_SPEED:
            self.y_speed = Constants.MAX_SPEED

    def check_for_offscreen(self):
        if self.x_pos < 0:
            self.x_pos = Constants.WINDOW_WIDTH
        if self.x_pos > Constants.WINDOW_WIDTH:
            self.x_pos = 0
        if self.y_pos < 0:
            self.y_pos = Constants.WINDOW_HEIGHT
        if self.y_pos > Constants.WINDOW_HEIGHT:
            self.y_pos = 0
            
    def move(self, dt, keys):
        if keys[0]:
            self.calc_speed()
        else:
            if abs(self.x_speed) - 0.02 <= 0:
                self.x_speed = 0
            elif self.x_speed < 0:
                self.x_speed += Constants.FRICTION * dt
            elif self.x_speed > 0:
                self.x_speed -= Constants.FRICTION * dt
            if abs(self.y_speed) - 0.02 <= 0:
                self.y_speed = 0
            elif self.y_speed < 0:
                self.y_speed += Constants.FRICTION * dt
            elif self.y_speed > 0:
                self.y_speed -= Constants.FRICTION * dt
        if keys[1]:
            self.rotation -= Constants.ROTATION_SPEED * dt
            if self.rotation < 0:
                self.rotation = 360
        if keys[2]:
            self.rotation += Constants.ROTATION_SPEED * dt
            if self.rotation > 360:
                self.rotation = 0
        self.x_pos += self.x_speed * dt
        self.y_pos += self.y_speed * dt
        self.check_for_offscreen()
        # print("ROTATION: " + str(self.rotation) + "; X_SPEED: " + str(self.x_speed) + "; Y_SPEED: " + str(self.y_speed))
        self.player.update(x=self.x_pos, y=self.y_pos, rotation=self.rotation)