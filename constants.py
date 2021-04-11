import pyglet

class Constants:
    # Window
    WINDOW_HEIGHT = 800
    WINDOW_WIDTH = 1200

    # Player
    MOVEMENT_SPEED = 20
    MAX_SPEED = 250
    ROTATION_SPEED = 250
    
    # Game
    FRICTION = 20
    BULLET_SPEED = 600
    BULLET_LIFETIME = 60

    # Space Objects (?)
    SMALL_ASTEROID_SPRITES = [pyglet.image.load("res/small/small_roid_1.png"), pyglet.image.load("res/small/small_roid_2.png"), pyglet.image.load("res/small/small_roid_3.png")]
    MEDIUM_ASTEROID_SPRITES = [pyglet.image.load("res/medium/medium_roid_1.png"), pyglet.image.load("res/medium/medium_roid_2.png"), pyglet.image.load("res/medium/medium_roid_3.png")]
    LARGE_ASTEROID_SPRITES = [pyglet.image.load("res/large/large_roid_1.png"), pyglet.image.load("res/large/large_roid_2.png"), pyglet.image.load("res/large/large_roid_3.png")]

    MIN_ASTEROID_SPEED = 50
    MAX_ASTEROID_SPEED = 350