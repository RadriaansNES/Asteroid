import pygame
from utils import load_sprite, get_random_position
from models import Spaceship, Asteroid

class SpaceRocks:
    ##add min distance to avoid init conflic
    MIN_ASTEROID_DISTANCE = 250
    ## Create class, initalize statements. Set display and background
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_sprite("space", False)
        # method to set fps value
        self.clock = pygame.time.Clock()
        # initialize gameobjects
        self.bullets = []
        self.spaceship = Spaceship((400, 300), self.bullets.append) # adding bullets 
        # randomize, intialize asteroid positions, set min distance
        self.asteroids = []
        for _ in range(6):
            #check position if larger than minimum, if not run again. Randomization here because one time process on boot
            while True:
                position = get_random_position(self.screen)
                if (position.distance_to(self.spaceship.position)> self.MIN_ASTEROID_DISTANCE):
                    break
            #update for asteroid generation
            self.asteroids.append(Asteroid(position, self.asteroids.append))
                
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
            ## add input for space bar (bullets)
            elif (
                self.spaceship
                and event.type == pygame.KEYDOWN
                and event.key == pygame.K_SPACE
            ):
                self.spaceship.shoot()
                
        # asign input to left and right keys
        if self.spaceship: #input handler check for prescense
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
        for game_object in self._get_game_objects():
            game_object.move(self.screen)
        #adding collision
        if self.spaceship:
            for asteroid in self.asteroids:
                if asteroid.collides_with(self.spaceship):
                    self.spaceship = None ## i.e. ships blown up
                    break
        #check if bullets coincide with original screen, if not in, remove        
        for bullet in self.bullets[:]:
            if not self.screen.get_rect().collidepoint(bullet.position):
                self.bullets.remove(bullet)
        #same as above, checking bullet and asteroid positions through collides with
        for bullet in self.bullets[:]:
            for asteroid in self.asteroids[:]:
                if asteroid.collides_with(bullet):
                    self.asteroids.remove(asteroid)
                    self.bullets.remove(bullet)
                    asteroid.split()
                    break

    ## Draw content to screen, here using background to draw space, objects
    def _draw(self):
        self.screen.blit(self.background, (0, 0))
        #loop  for multiple objects, drawing
        for game_object in self._get_game_objects():
            game_object.draw(self.screen)
        pygame.display.flip()
        # run 60fps
        self.clock.tick(60)
    
    ## method to move/return game objects
    def _get_game_objects(self):
        game_objects = [*self.asteroids, *self.bullets]

        if self.spaceship:  #check for being present
            game_objects.append(self.spaceship) 

        return game_objects