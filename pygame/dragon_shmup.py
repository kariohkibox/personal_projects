import sys, pygame, random

size = width, height = 1024, 576
black = 10,10,10
red = 250,0,0
fps = 60

pygame.init()
pygame.display.set_caption("dragon shmup")
clock = pygame.time.Clock()

screen = pygame.display.set_mode(size)

class Dragon(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.transform.scale((pygame.image.load('dragon_2.png')), (150, 80))
   # self.image.fill(red)
    self.rect = self.image.get_rect()
    self.rect.centerx = 100
    self.rect.bottom = height / 2
    self.speedy = 0

  def update(self):
    self.speedy = 0
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_UP]:
      self.speedy = -5
    if keystate[pygame.K_DOWN]:
      self.speedy = 5
    self.rect.y += self.speedy
    if self.rect.top < 0:
      self.rect.top = 0
    if self.rect.bottom > height:
      self.rect.bottom = height

all_sprites = pygame.sprite.Group()
player = Dragon()
all_sprites.add(player)

# dragon = pygame.transform.scale((pygame.image.load('dragon_2.png')), (150, 80))
# dragon_rect = dragon.get_rect(topright=(width, 0))

while 1:
  clock.tick(fps)
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()

  all_sprites.update()

  screen.fill(black)
#  screen.blit(dragon, dragon_rect)
  all_sprites.draw(screen)
  pygame.display.flip()