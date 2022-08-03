import functions
import pygame
from functions import *

# Create screen and background color
pygame.display.set_caption("Magic Casters")
WINDOW_SIZE = (1200, 800)
backgroundColor = 20, 20, 20

# Load all relevant images
player_image = pygame.image.load('Characters/knight/idle/idle_1.png')
floor_image = pygame.image.load('Tiles/floor_tile_3.png')
brick_image = pygame.image.load('Tiles/brick_1.png')

idle_images = [pygame.image.load('Characters/knight/idle/idle_1.png'),
               pygame.image.load('Characters/knight/idle/idle_2.png'),
               pygame.image.load('Characters/knight/idle/idle_3.png'),
               pygame.image.load('Characters/knight/idle/idle_4.png'),
               pygame.image.load('Characters/knight/idle/idle_5.png'),
               pygame.image.load('Characters/knight/idle/idle_6.png')]

# blank = pygame.image.load('Tiles/blank.png')
# Set width of tiles for generation
TILE_SIZE = brick_image.get_width()
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
# Create display for pixel scaling
display = pygame.Surface((600, 400))

game_map = read_map('map')

# Default movement
moving_right = False
moving_left = False

# Player movement and hitboxes
player_y_momentum = 0
air_timer = 0
camera_scroll = [0, 0]
player_rect = pygame.Rect(300, 300, player_image.get_width(), player_image.get_height())

frame = 0
image_interval = 100
last_update = 0