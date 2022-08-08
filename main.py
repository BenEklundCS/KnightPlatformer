import pygame, sys, os
from functions import *
from assets import *

clock = pygame.time.Clock()

from pygame.locals import *

pygame.init()

while True:

    display.fill(backgroundColor)

    camera_scroll[0] += (player_rect.x - camera_scroll[0] - 200) / 20
    camera_scroll[1] += (player_rect.y - camera_scroll[1] - 200) / 20
    scroll = camera_scroll.copy()
    scroll[0] = int(scroll[0])
    scroll[1] = int(scroll[1])

    # Render Tile Map
    tile_rects = []
    y = 0
    for row in game_map:
        x = 0
        for tile in row:
            if tile == '1':
                display.blit(floor_image, (x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1]))
            if tile == '2':
                display.blit(brick_image, (x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1]))
            if tile != '0':
                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            x += 1
        y += 1

    # Player movement handling
    player_movement = [0, 0]  # by default the player should not be moving without input
    if moving_right:
        player_movement[0] += 5  # when player is moving right we change the x velocity by a positive number
    if moving_left:
        player_movement[0] -= 5  # when player is moving right we change the x velocity by a negative number
    player_movement[1] += player_y_momentum
    player_y_momentum += 0.2  # y velocity should always be resisted by gravity
    if player_y_momentum > 3:  # terminal velocity
        player_y_momentum = 3
    # Run move function to determine player_rect movement
    player_rect, collisions = move(player_rect, player_movement, tile_rects)
    if collisions['bottom']:  # stops player from falling through the floor as well as reset of the air timer
        player_y_momentum = 0
        air_timer = 0
    else:
        air_timer += 1

    # Display player/refresh and animations
    if moving_right or moving_left:
        if frame >= len(walk_images):
            frame = 0
        player_image = walk_images[frame]
        if pygame.time.get_ticks() - last_update > image_interval - 75:
            frame += 1
            last_update = pygame.time.get_ticks()
    else:
        if frame >= len(idle_images):
            frame = 0
        player_image = idle_images[frame]
        if pygame.time.get_ticks() - last_update > image_interval:
            frame += 1
            last_update = pygame.time.get_ticks()

    if reverse:
      player_image = pygame.transform.flip(player_image, True, False)
    display.blit(player_image, (player_rect.x - camera_scroll[0], player_rect.y - camera_scroll[1]))

    # Game event loop
    for event in pygame.event.get():  # event loop
        if event.type == pygame.QUIT:  # check for window quit
            pygame.quit()  # stop pygame
            sys.exit()  # stop script
        # Player controls
        if event.type == KEYDOWN:  # check for key pressed and alter movement based on it
            if event.key == K_RIGHT:
                moving_right = True
                reverse = False
            if event.key == K_LEFT:
                moving_left = True
                reverse = True
            if event.key == K_UP:
                if air_timer < 6:  # this prevents "spamming" the jump key to multi-jump
                    player_y_momentum = -6
        if event.type == KEYUP:  # check for key released and alter movement based on it
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False

    # Display draw and updates
    surf = pygame.transform.scale(display, WINDOW_SIZE)
    screen.blit(surf, (0, 0))
    pygame.display.update()
    clock.tick(60)
