from pygame.math import Vector2

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
    def move(self):
        self.position = self.position + self.velocity
# detect collision of sprites
    def collides_with(self, other_obj):
        distance = self.position.distance_to(other_obj.position)
        return distance < self.radius + other_obj.radius