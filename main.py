import pygame, time

pygame.init()
width, height = 640, 480
backgroundColor = 0, 0, 0

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Magic Casters")

while True:
	screen.fill(backgroundColor)
	pygame.display.flip()

def main():
  while True:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              return
main()