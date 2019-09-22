import sys, pygame
pygame.init()

size = width, height = 1024, 576
black = 0,155,0

screen = pygame.display.set_mode(size)

character_size = 10
up = (0, -character_size)
down = (0, character_size)
left = (-character_size, 0)
right = (character_size, 0)

dragon = pygame.transform.scale((pygame.image.load('dragon_2.png')), (153, 81))
dragon_rect = dragon.get_rect(topright=(width, 0))

while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()
    
  screen.fill(black)
  screen.blit(dragon, dragon_rect)
  pygame.display.flip()