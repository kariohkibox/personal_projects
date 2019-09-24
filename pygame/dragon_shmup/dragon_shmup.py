import sys, pygame, random, os
import dragon, enemy, fireball, powerup

pygame.init()

size = width, height = 1024, 576
black = 0, 0, 0
green = 0, 210, 0
fps = 30

screen = pygame.display.set_mode(size)
bgOne = pygame.image.load(os.path.join("img", "cloud_bg.jpg")).convert()
bgTwo = pygame.image.load(os.path.join("img", "cloud_bg.jpg")).convert()
player_mini_img = pygame.transform.scale((pygame.image.load(os.path.join("img", "dragon_2.png"))), (40, 21))
player_mini_img.set_colorkey(black)

bgX = 0
bgX2 = bgOne.get_width()

pygame.display.set_caption("dragon shmup")
clock = pygame.time.Clock()
previous_time = pygame.time.get_ticks()
font_name = pygame.font.match_font("Calibri")

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
fireballs = pygame.sprite.Group()
powerups = pygame.sprite.Group()

player = dragon.Dragon()
all_sprites.add(player)


# make the score text
def draw_text(surf, text, fsize, x, y):
    font = pygame.font.Font(font_name, fsize)
    text_surface = font.render(text, True, black)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


# spawns new enemy
def new_enemy():
    e = enemy.Enemy()
    all_sprites.add(e)
    enemies.add(e)


# make the health bar
def draw_health_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    bar_length = 100
    bar_height = 10
    fill = (pct / 100) * bar_length
    outline_rect = pygame.Rect(x, y, bar_length, bar_height)
    fill_rect = pygame.Rect(x, y, fill, bar_height)
    pygame.draw.rect(surf, green, fill_rect)
    pygame.draw.rect(surf, black, outline_rect, 2)


# make the lives counter
def draw_lives(surf, x, y, lives, img):
    for j in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 45 * j
        img_rect.y = y
        surf.blit(img, img_rect)


# spawns enemies
for i in range(5):
    new_enemy()

# init score variable for tracking
score = 0

# game loop
running = True
while running:
    clock.tick(fps)
    keystate = pygame.key.get_pressed()
    current_time = pygame.time.get_ticks()
    if keystate[pygame.K_SPACE]:
        if current_time - previous_time > 500:
            previous_time = current_time
            if player.power == 1:
                fire = fireball.Fireball()
                fire.rect.left = player.rect.right
                fire.rect.centery = player.rect.centery
                all_sprites.add(fire)
                fireballs.add(fire)
            if player.power >= 2:
                fire1 = fireball.Fireball()
                fire2 = fireball.Fireball()
                fire1.rect.left = player.rect.right
                fire2.rect.left = player.rect.right
                fire1.rect.centery = player.rect.centery - 18
                fire2.rect.centery = player.rect.centery + 18
                all_sprites.add(fire1)
                all_sprites.add(fire2)
                fireballs.add(fire1)
                fireballs.add(fire2)

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
    bgX -= 9
    bgX2 -= 9

    if bgX <= -1 * bgOne.get_width():
        bgX = bgX2 + bgTwo.get_width()
    if bgX2 <= -1 * bgTwo.get_width():
        bgX2 = bgX + bgOne.get_width()

    # Update
    all_sprites.update()

    # check if fireball hits enemy
    hits = pygame.sprite.groupcollide(enemies, fireballs, True, True, pygame.sprite.collide_rect_ratio(0.5))
    for hit in hits:
        score += 5
        new_enemy()
        if random.random() > 0.9:
            power = powerup.Pow(hit.rect.center)
            all_sprites.add(power)
            powerups.add(power)

    # check if player hits enemy
    hits = pygame.sprite.spritecollide(player, enemies, True, pygame.sprite.collide_rect_ratio(0.7))
    for hit in hits:
        player.health -= 10
        new_enemy()
        if player.health <= 0:
            player.hide()
            player.lives -= 1
            player.health = 100

    # check if player hits powerup
    hits = pygame.sprite.spritecollide(player, powerups, True)
    for hit in hits:
        if hit.type == 'health':
            player.health += 10
            if player.health >= 100:
                player.health = 100
        if hit.type == 'weapon':
            player.powerup()

    # end game if player has no lives
    if player.lives == 0:
        running = False

    screen.fill(black)
    screen.blit(bgOne, (bgX, 0))
    screen.blit(bgTwo, (bgX2, 0))
    all_sprites.draw(screen)
    draw_text(screen, str(score), 24, width/2, 10)
    draw_health_bar(screen, 10, 10, player.health)
    draw_lives(screen, width - 150, 10, player.lives, player_mini_img)

    pygame.display.flip()
