import pygame
import sys
from pygame import locals as lc
from random import randint


class Player(pygame.sprite.Sprite):

    def __init__(self, start_x, start_y, width, height):
        pass

    def move_y(self):
        pass

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
# Initialize pygame.mixer
# Initialize pygame
# Load level
# Initialize variables
finished = False
# Setup the background
while not finished:
    pass
    # Blank screen
    # Check events
    # Check which keys are held
    # Move the player with gravity
    # Rander the frame
    # Update the display
    # Check if the player is dead
    # Check if the player has completed the level
    # Set the speed
