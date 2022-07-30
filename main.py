import pygame, sys, os

clock = pygame.time.Clock()

from pygame.locals import *

pygame.init()

# Create screen and background color
pygame.display.set_caption("Magic Casters")
WINDOW_SIZE = (1200, 800)
backgroundColor = 0, 60, 120

# Load all relevant images
player_image = pygame.image.load(os.path.join('Characters/knight/idle', 'idle_knight_1.png'))
floor_image = pygame.image.load('Tiles/floor_tile_3.png')
brick_image = pygame.image.load('Tiles/brick_1.png')
# Set width of tiles for generation 
TILE_SIZE = brick_image.get_width()
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
# Create display for pixel scaling
display = pygame.Surface((600, 400))


# Generate/read game map
def read_map(path):
    f = open(path + '.txt', 'r')
    data = f.read()
    f.close()
    data = data.split('\n')
    game_map = []
    for row in data:
        game_map.append(list(row))
    return game_map


game_map = read_map('map')


# Collision and movement functions
def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list


def move(rect, movement, tiles):
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    rect.x += movement[0]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
    rect.y += movement[1]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect, collision_types


# Default movement
moving_right = False
moving_left = False

# Player movement and hitboxes
player_y_momentum = 0
air_timer = 0
camera_scroll = [0, 0]
player_rect = pygame.Rect(50, 50, player_image.get_width(), player_image.get_height())

while True:

    display.fill(backgroundColor)

    camera_scroll[0] += (player_rect.x-camera_scroll[0]-200)/20
    camera_scroll[1] += (player_rect.y-camera_scroll[1]-200)/20
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
                display.blit(floor_image, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
            if tile == '2':
                display.blit(brick_image, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
            if tile != '0':
                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            x += 1
        y += 1

    # player_location[1] += player_y_momentum
    # Player movement handling
    player_movement = [0, 0]  # by default the player should not be moving without input
    if moving_right:
        player_movement[0] += 3  # when player is moving right we change the x velocity by a positive number
    if moving_left:
        player_movement[0] -= 3  # when player is moving right we change the x velocity by a negative number
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
    # Display player/refresh
    display.blit(player_image, (player_rect.x-camera_scroll[0], player_rect.y-camera_scroll[1]))

    # Game event loop
    for event in pygame.event.get():  # event loop
        if event.type == pygame.QUIT:  # check for window quit
            pygame.quit()  # stop pygame
            sys.exit()  # stop script
        # Player controls
        if event.type == KEYDOWN:  # check for key pressed and alter movement based on it
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
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
