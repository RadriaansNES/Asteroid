from pygame.image import load
from pygame.math import Vector2
from pygame.mixer import Sound
from pygame import Color
import random

# Loads image as surface. If with alpha reflects transparency
def load_sprite(name, with_alpha=True):
    path = f"assets/sprites/{name}.png"
    loaded_sprite = load(path)

    if with_alpha:
        return loaded_sprite.convert_alpha()
    else:
        return loaded_sprite.convert()
# function to wrap objects back around the screen
def wrap_position(position, surface):
    x, y = position
    w, h = surface.get_size()
    return Vector2(x % w, y % h)

#create random position for asteroids
def get_random_position(surface):
    return Vector2(
        random.randrange(surface.get_width()),
        random.randrange(surface.get_height()),
    )

# random method for velocities
def get_random_velocity(min_speed, max_speed):
    speed = random.randint(min_speed, max_speed)
    angle = random.randrange(0, 360)
    return Vector2(speed, 0).rotate(angle)

# method for sound
def load_sound(name):
    path = f"assets/sounds/{name}.wav"
    return Sound(path)

# draw text to center
def print_text(surface, text, font, color=Color("firebrick1")):
    text_surface = font.render(text, True, color)
    rect = text_surface.get_rect()
    rect.center = Vector2(surface.get_size()) / 2
    surface.blit(text_surface, rect)