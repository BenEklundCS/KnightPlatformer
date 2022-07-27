import pygame, time, sys

clock = pygame.time.Clock()

from pygame.locals import *

pygame.init()
pygame.display.set_caption("Magic Casters")
WINDOW_SIZE = (640, 480)
backgroundColor = 0, 0, 0

screen = pygame.display.set_mode((WINDOW_SIZE),0,32)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      return
      
  screen.fill(backgroundColor)
  pygame.display.flip()
  clock.tick(60)
  
def main():

main()