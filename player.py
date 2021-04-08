import pyglet

class Player: 
    x_pos = 400
    y_pos = 400
    speed = 10
    player_img = pyglet.image.load("player.png")
    player = pyglet.sprite.Sprite(player_img, x=x_pos, y=y_pos)

    # def __init__(self):
    #     self.player.update(scale=0.75)

    def draw(self):
        self.player.draw()

    def move(self, key):
        if key == 119:
            self.y_pos += self.speed
        if key == 97:
            self.x_pos -= self.speed
        if key == 115:
            self.y_pos -= self.speed
        if key == 100:
            self.x_pos += self.speed
        self.player.update(x=self.x_pos, y=self.y_pos)