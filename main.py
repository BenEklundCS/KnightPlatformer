import pygame, time, sys, os

clock = pygame.time.Clock()

from pygame.locals import *

pygame.init()
pygame.display.set_caption("Magic Casters")
WINDOW_SIZE = (800, 600)
backgroundColor = 0, 60, 120

player_image = pygame.image.load(os.path.join('Characters/knight/idle','idle_knight_1.png'))
floor_image = pygame.image.load('Tiles/floor_tile_3.png')
brick_image = pygame.image.load('Tiles/brick_1.png')
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
display = pygame.Surface((400, 300))

game_map = [['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2'],
            ['2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2'],
            ['2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2'],
            ['2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2']]

moving_right = False
moving_left = False

player_location = [50,50]
player_y_momentum = 0
#player_rect = pygame.rect(player_location[0],player_location[1],player_image.get_width(),player_image.get_height())

while True:

    display.fill(backgroundColor)

    display.blit(player_image,player_location)

    player_y_momentum += 0.2
    player_location[1] += player_y_momentum

    if moving_right:
        player_location[0] += 4
    if moving_left:
        player_location[0] -= 4

    #player_rect.x = player_location[0]
    #player_rect.y = player_location[1]


    for event in pygame.event.get():  # event loop
        if event.type == pygame.QUIT:  # check for window quit
            pygame.quit()  # stop pygame
            sys.exit()  # stop script
        if event.type == KEYDOWN:  # check for key pressed
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
        if event.type == KEYUP:  # check for key released
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False

    surf = pygame.transform.scale(display, WINDOW_SIZE)
    screen.blit(surf, (0, 0))
    pygame.display.update()
    clock.tick(60)


def main():
    pass
main()            