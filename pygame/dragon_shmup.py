import sys, pygame, random
import dragon, enemy, fireball

size = width, height = 1024, 576
black = 10, 10, 10
fps = 30

pygame.init()
pygame.display.set_caption("dragon shmup")
clock = pygame.time.Clock()
previous_time = pygame.time.get_ticks()

screen = pygame.display.set_mode(size)

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
fireballs = pygame.sprite.Group()

player = dragon.Dragon()
all_sprites.add(player)


for i in range(5):
    e = enemy.Enemy()
    all_sprites.add(e)
    enemies.add(e)

# game loop
running = True
while running:
    clock.tick(fps)
    keystate = pygame.key.get_pressed()
    current_time = pygame.time.get_ticks()
    if keystate[pygame.K_SPACE]:
        if current_time - previous_time > 500:
            previous_time = current_time
            fire = fireball.Fireball()
            fire.rect.left = player.rect.right
            fire.rect.centery = player.rect.centery
            all_sprites.add(fire)
            fireballs.add(fire)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         fire = fireball.Fireball()
        #         fire.rect.left = player.rect.right
        #         fire.rect.centery = player.rect.centery
        #         all_sprites.add(fire)
        #         fireballs.add(fire)

    # Update
    all_sprites.update()

    # check enemy to player collision
    # hits = pygame.sprite.spritecollide(player, enemies, False)
    # if hits:
    #     running = False

    # check if fireball hits enemy
    hits = pygame.sprite.groupcollide(enemies, fireballs, True, True)
    for hit in hits:
        e = enemy.Enemy()
        all_sprites.add(e)
        enemies.add(e)

    screen.fill(black)
    all_sprites.draw(screen)
    pygame.display.flip()
