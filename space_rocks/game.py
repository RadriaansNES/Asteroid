import pygame
from utils import load_sprite
from models import Spaceship

class SpaceRocks:
    ## Create class, initalize statements. Set display and background
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_sprite("space", False)
        # method to set fps value
        self.clock = pygame.time.Clock()
    # initialize gameobjects
        self.spaceship = Spaceship((400, 300))

    ## Reg game loop method
    def main_loop(self):
        while True:
            self._handle_input()
            self._process_game_logic()
            self._draw()

    ## Starts pygame
    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Space Rocks")

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()
        # asign input to left and right keys
        is_key_pressed = pygame.key.get_pressed()
        if is_key_pressed[pygame.K_RIGHT]:
            self.spaceship.rotate(clockwise=True)
        elif is_key_pressed[pygame.K_LEFT]:
            self.spaceship.rotate(clockwise=False)
        if is_key_pressed[pygame.K_UP]:
            self.spaceship.accelerate()
        if is_key_pressed[pygame.K_DOWN]:
            self.spaceship.slow()

    ## Updates each  frame
    def _process_game_logic(self):
        self.spaceship.move(self.screen)

    ## Draw content to screen, here using background to draw space, objects
    def _draw(self):
        self.screen.blit(self.background, (0, 0))
        self.spaceship.draw(self.screen)
        pygame.display.flip()
        # run 60fps
        self.clock.tick(60)