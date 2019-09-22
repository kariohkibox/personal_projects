import sys, pygame, random
import dragon

size = width, height = 1024, 576
black = 10, 10, 10
red = 250, 0, 0
fps = 60

pygame.init()
pygame.display.set_caption("dragon shmup")
clock = pygame.time.Clock()

screen = pygame.display.set_mode(size)

player = dragon.Dragon()
all_sprites = pygame.sprite.Group(player)

while 1:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    all_sprites.update()

    screen.fill(black)
    all_sprites.draw(screen)
    pygame.display.flip()
