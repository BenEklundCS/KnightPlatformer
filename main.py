import pygame, sys, os
from functions import *
from assets import *

clock = pygame.time.Clock()

from pygame.locals import *

pygame.init()

while True:

    display.blit(background_image, (0, 0))

    camera_scroll[0] += (player_rect.x - camera_scroll[0] - 350) / 20
    camera_scroll[1] += (player_rect.y - camera_scroll[1] - 350) / 20
    scroll = camera_scroll.copy()
    scroll[0] = int(scroll[0])
    scroll[1] = int(scroll[1])
    """
    
    # Render Tile Map
    
    """
    tile_rects = []
    for y in range(6):
        for x in range(6):
            target_x = x - 1 + int(round(scroll[0]/(CHUNK_SIZE*32)))
            target_y = y - 1 + int(round(scroll[1]/(CHUNK_SIZE*32)))
            target_chunk = str(target_x) + ";" + str(target_y)
            if target_chunk not in game_map:
                game_map[target_chunk] = generate_chunk(target_x, target_y)
            for tile in game_map[target_chunk]:
                display.blit(tile_index[tile[1]], (tile[0][0]*32-scroll[0], tile[0][1]*32-scroll[1]))
                if tile[1] in [1,2]:
                    tile_rects.append(pygame.Rect(tile[0][0]*32, tile[0][1]*32, 32, 32))
    """
    
    # Player movement handling
    
    """
    player_movement = [0, 0]  # by default the player should not be moving without input
    if moving_right:
        player_movement[0] += 4  # when player is moving right we change the x velocity by a positive number
    if moving_left:
        player_movement[0] -= 4  # when player is moving right we change the x velocity by a negative number
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
    """

    # Display player/refresh and animations
    
    """
    if moving_right and air_timer < 6 or moving_left and air_timer < 6:
        if frame >= len(walk_images):
            frame = 0
        player_image = walk_images[frame]
        if pygame.time.get_ticks() - last_update > image_interval - 75:
            frame += 1
            last_update = pygame.time.get_ticks()
    elif air_timer > 6:
        if frame >= len(jump_images):
            frame = 0
        player_image = jump_images[frame]
        if pygame.time.get_ticks() - last_update > image_interval:
            frame += 1
            last_update = pygame.time.get_ticks()
    else:
        if frame >= len(idle_images):
            frame = 0
        player_image = idle_images[frame]
        if pygame.time.get_ticks() - last_update > image_interval:
            frame += 1
            last_update = pygame.time.get_ticks()
    """
    
    # Player image reverse handling

    """
    if reverse:
      player_image = pygame.transform.flip(player_image, True, False)
    display.blit(player_image, (player_rect.x - camera_scroll[0], player_rect.y - camera_scroll[1]))
    """
    
    # Game event loop
    
    """
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
            #if event.key == K_DOWN:
            #add slide mechanic
        if event.type == KEYUP:  # check for key released and alter movement based on it
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False
    """
    
    # Display draw and updates
    
    """
    surf = pygame.transform.scale(display, WINDOW_SIZE)
    screen.blit(surf, (0, 0))
    pygame.display.update()
    clock.tick(60)
