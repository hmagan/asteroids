from pyglet import shapes

class Bullet:
    x = -1
    y = -1
    x_diff = -1
    y_diff = -1
    speed = 5
    bullet = shapes.Circle(200, 300, 5, color=(155, 0, 0))

    def __init__(self, x, y, x_diff, y_diff, batch):
        self.x = x
        self.y = y
        self.x_diff = x_diff
        self.y_diff = y_diff

        self.bullet = shapes.Circle(x, y, 20, color=(155, 0, 0), batch=batch)

        self.bullet.draw()