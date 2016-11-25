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

        collided_y = world.collided_get_y(self.base)

        if self.speed_y <= 0 or collided_y < 0:

            self.rect.y = self.rect.y + self.speed_y
            self.speed_y = self.speed_y + gravity

        if collided_y > 0 and self.speed_y > 0:

            self.rect.y = collided_y

        self.base.y = self.rect.y + self.rect.height

    def jump(self, speed):

        if world.collided_get_y(self.base) > 0:

            self.speed_y = speed


class World():

    def __init__(self, level, block_size, color_platform, color_goals):

        self.platforms = []
        self.goals = []
        self.posn_y = 0
        self.color = color_platform
        self.color_goals = color_goals
        self.block_size = block_size

        # Draw the world according to level
        for line in level:

            self.posn_x = 0

            for block in line:

                if block == '-':
                    self.platforms.append(pygame.Rect(self.posn_x, self.posn_y, block_size, block_size))

                if block == 'G':
                    self.goals.append(pygame.Rect(self.posn_x, self.posn_y, block_size, block_size))

                self.posn_x = self.posn_x + block_size

            self.posn_y = self.posn_y + block_size

    def move(self, dist):

        for block in self.platforms + self.goals:

            block.move_ip(dist, 0)

    def collided_get_y(self, player_rect):

        return_y = -1

        for block in self.platforms:

            if block.colliderect(player_rect):

                return_y = block.y - block.height + 1

        return return_y

    def at_goal(self, player_rect):

        for block in self.goals:

            if block.colliderect(player_rect):

                return True

        return False

    def update(self, screen):

        for block in self.platforms:

            pygame.draw.rect(screen, self.color, block, 0)

        for block in self.goals:

            pygame.draw.rect(screen, self.color_goals, block, 0)


class Doom():

    def __init__(self, fireball_num, pit_depth, color):

        self.base = pygame.Rect(0, screen_y - pit_depth, screen_x, pit_depth)
        self.color = color
        self.fireballs = []

        for i in range(0, fireball_num):

            self.fireballs.append(Fireball())

        self.fireball_plain = pygame.sprite.RenderPlain(self.fireballs)

    def move(self, dist):

        for fireball in self.fireballs:

            fireball.move_x(dist)

    def update(self, screen):

        for fireball in self.fireballs:

            fireball.move_y()

        self.fireball_plain.draw(screen)
        pygame.draw.rect(screen, self.color, self.base, 0)

    def collided(self, player_rect):

        for fireball in self.fireballs:

            if fireball.rect.colliderect(player_rect):

                hit_box = fireball.rect.inflate(-int(fireball_size / 2), -int(fireball_size / 2))

                if hit_box.colliderect(player_rect):

                    return True

        return self.base.colliderect(player_rect)


class Fireball(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(fireball_image), (fireball_size, fireball_size))
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):

        self.y = 0
        self.speed_y = randint(fireball_low_speed, fireball_high_speed)
        self.x = randint(0, screen_x)
        self.rect.topleft = (self.x, self.y)

    def move_x(self, dist):

        self.rect.move_ip(dist, 0)

        if self.rect.x < -50 or self.rect.x > screen_x:

            self.reset()

    def move_y(self):

        self.rect.move_ip(0, self.speed_y)

        if self.rect.y > screen_y:

            self.reset()

    def update(self, screen, color):
        pass


# Options
screen_x, screen_y = 600, 400
game_name = 'Awesome Raspberry Pi Platformer'

player_spawn_x, player_spawn_y = 50, 200
player_image = 'lidia.png'

level = [
    "                              ",
    "                              ",
    "                              ",
    "                              ",
    "                              ",
    "                              ",
    "                              ",
    "          ---                G",
    "     -- --    ---       ------",
    " -- -            -------      "
]
platform_color = (100, 100, 100)
goal_color = (0, 0, 255)

gravity = 1

jump_speed = -10

doom_color = (255, 0, 0)

fireball_size = 30
fireball_number = 10
fireball_low_speed = 3
fireball_high_speed = 7
fireball_image = 'flame.png'

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

world = World(level, 30, platform_color, goal_color)

doom = Doom(fireball_number, 10, doom_color)

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
    key_state = pygame.key.get_pressed()

    if key_state[lc.K_LEFT]:

        world.move(2)
        doom.move(2)

    elif key_state[lc.K_RIGHT]:

        world.move(-2)
        doom.move(-2)

    if key_state[lc.K_SPACE]:

        player.jump(jump_speed)

    # Move the player with gravity
    player.move_y()

    # Render the frame
    player_plain.draw(screen)
    world.update(screen)
    doom.update(screen)

    # Update the display
    pygame.display.update()

    # Check if the player is dead
    if doom.collided(player.rect):

        print('You Lose!')
        finished = True

    # Check if the player has completed the level
    if world.at_goal(player.rect):

        print('Winner!')
        finished = True

    # Set the speed
    clock.tick(20)
