import pygame
from utils import load_sprite
from models import GameObject

class SpaceRocks:
    ## Create class, initalize statements. Set display and background
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_sprite("space", False)
        # method to set fps value
        self.clock = pygame.time.Clock()
    # initialize gameobjects
        self.spaceship = GameObject(
            (400, 300), load_sprite("spaceship"), (0, 0)
        )
        self.asteroid = GameObject(
            (400, 300), load_sprite("asteroid"), (1, 0)
        )

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
    ## Updates each  frame
    def _process_game_logic(self):
        self.spaceship.move()
        self.asteroid.move()

    ## Draw content to screen, here using background to draw space, objects
    def _draw(self):
        self.screen.blit(self.background, (0, 0))
        self.spaceship.draw(self.screen)
        self.asteroid.draw(self.screen)
        pygame.display.flip()
        # run 60fps
        self.clock.tick(60)