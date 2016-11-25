import pygame
import sys
from pygame import locals as lc
from random import randint


class Player(pygame.sprite.Sprite):

    def __init__(self, start_x, start_y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(player_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y
        self.speed_y = 0
        self.base = pygame.Rect(start_x, start_y + height, width, 2)

    def move_y(self):
        self.rect.y = self.rect.y + 1

    def jump(self, speed):
        pass


class World():

    def __init__(self, level, block_size, color_platform, color_goals):
        pass

    def move(self, dist):
        pass

    def collided_get_y(self, player_rect):
        pass

    def at_goal(self, player_rect):
        pass

    def update(self, screen):
        pass


class Doom():

    def __init__(self, fireball_num, pit_depth, color):
        pass

    def move(self, dist):
        pass

    def update(self, screen):
        pass

    def collided(self, player_rect):
        pass


class Fireball(pygame.sprite.Sprite):

    def __init__(self):
        pass

    def reset(self):
        pass

    def move_x(self, dist):
        pass

    def move_y(self):
        pass

    def update(self, screen, color):
        pass


# Options
screen_x, screen_y = 600, 400
game_name = 'Awesome Raspberry Pi Platformer'

player_spawn_x, player_spawn_y = 50, 200
player_image = 'lidia.png'

# Initialize pygame.mixer

# Initialize pygame
pygame.init()
window = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption(game_name)
screen = pygame.display.get_surface()

# Load level
# Initialize variables
finished = False
clock = pygame.time.Clock()

player = Player(player_spawn_x, player_spawn_y, 20, 30)
player_plain = pygame.sprite.RenderPlain(player)

# Setup the background
# Each loop is a frame
while not finished:

    # Blank screen
    screen.fill((0, 0, 0))

    # Check events
    for event in pygame.event.get():
        if event.type == lc.QUIT:
            finished = True

    # Check which keys are held
    # Move the player with gravity
    player.move_y()

    # Render the frame
    player_plain.draw(screen)

    # Update the display
    pygame.display.update()

    # Check if the player is dead
    # Check if the player has completed the level
    # Set the speed
    clock.tick(20)
