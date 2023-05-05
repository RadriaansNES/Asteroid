from pygame.math import Vector2
from utils import load_sprite, wrap_position, get_random_velocity
from pygame.transform import rotozoom

UP = Vector2(0, -1)

## Creation of gameobject, which will encapsulate generic behaviour and data for game objects
class GameObject:
    def __init__(self, position, sprite, velocity):
        self.position = Vector2(position)
        self.sprite = sprite
        self.radius = sprite.get_width() / 2
        self.velocity = Vector2(velocity)
# draw sprite to surface
    def draw(self, surface):
        blit_position = self.position - Vector2(self.radius)
        surface.blit(self.sprite, blit_position)
# update position of game object
    def move(self, surface):
        #add constructor to wrap over screen
        self.position = wrap_position(self.position + self.velocity, surface)
# detect collision of sprites
    def collides_with(self, other_obj):
        distance = self.position.distance_to(other_obj.position)
        return distance < self.radius + other_obj.radius
    

## Space object inherited from gameobject
class Spaceship(GameObject):
    MANEUVERABILITY = 3
    ACCELERATION = 0.1
    BULLET_SPEED = 3
    #init spaceship image, zero velocity. bullet callbacks
    def __init__(self, position, create_bullet_callback):
        self.create_bullet_callback = create_bullet_callback 
        # init vector direction of rotation
        self.direction = Vector2(UP)
        super().__init__(position, load_sprite("spaceship"), Vector2(0))
    # defining rotating method
    def rotate(self, clockwise=True):
        sign = 1 if clockwise else -1
        angle = self.MANEUVERABILITY * sign
        # rotate via given angle (Degrees)
        self.direction.rotate_ip(angle)
    # draw spaceship to surface
    def draw(self, surface):
        angle = self.direction.angle_to(UP)
        rotated_surface = rotozoom(self.sprite, angle, 1.0)
        rotated_surface_size = Vector2(rotated_surface.get_size())
        blit_position = self.position - rotated_surface_size * 0.5
        surface.blit(rotated_surface, blit_position)
    # create acceleration method
    def accelerate(self):
        self.velocity += self.direction * self.ACCELERATION
    # create slowdown thruster method
    def slow(self):
        self.velocity -= self.direction * self.ACCELERATION
    # create shoot method
    def shoot(self):
        bullet_velocity = self.direction * self.BULLET_SPEED + self.velocity
        bullet = Bullet(self.position, bullet_velocity)
        self.create_bullet_callback(bullet)

## create asteroid class
class Asteroid(GameObject):
    def __init__(self, position):
        # random velocity 
        super().__init__(position, load_sprite("asteroid"), get_random_velocity(1, 3))

## create bullet class
class Bullet(GameObject):
    def __init__(self, position, velocity):
        super().__init__(position, load_sprite("bullet"), velocity)