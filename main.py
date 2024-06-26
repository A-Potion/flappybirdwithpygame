import sys, pygame, random, os
pygame.init()

def load_image(name, scale):
    fullpath = os.path.join(data_dir, name)
    image = pygame.image.load(fullpath)

    size = image.get_size()
    size = size[0] * scale, size[1] * scale
    image = pygame.transform.scale(image, size)

    return image, image.get_rect()

class Bird(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("bird.png", 0.35)
        self.rect.x, self.rect.y = (screen.get_width() / 2) - (self.image.get_size()[0] / 2), (screen.get_height() / 2) - (self.image.get_size()[1] / 2)
        self.area = self.rect

    def up(self):
        self.rect.y += -300 * dt

class Cloud(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("cloud.png", random.uniform(0.1, 0.2))
        self.rect.topleft = 1000, random.uniform(0, 100)

main_dir = os.path.split(os.path.abspath(__file__))[0]
print(main_dir)
data_dir = os.path.join(main_dir, "assets")

size = width, height = 1000, 600
bird_speed = [0, 2]
cloud_speed = (-1, 0)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
dt = 0

cloud = Cloud()

bird = Bird()

while running:
    screen.blit(bird.image, bird.rect)
    screen.blit(cloud.image, cloud.rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    cloud.rect = cloud.rect.move(cloud_speed)

    print(cloud.rect.x, cloud.rect.y)

    screen.fill("blue")

    bird.rect = bird.rect.move(bird_speed)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if bird.rect.top <= 0:
            bird.rect.y += -2
        else:
            bird.up()
    elif bird.rect.bottom >= height:
        bird.rect.y += -2


    screen.blit(bird.image, bird.rect)
    screen.blit(cloud.image, cloud.rect)
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()