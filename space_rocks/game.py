import pygame
from utils import load_sprite

class SpaceRocks:
    ## Create class, initalize statements. Set display and background
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_sprite("space", False)

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

    def _process_game_logic(self):
        pass

    ## Draw content to screen, here using background to draw space
    def _draw(self):
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()