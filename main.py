import sys, pygame, random, os
pygame.init()

def load_image(name, scale):
    fullpath = os.path.join(data_dir, name)
    image = pygame.image.load(fullpath)

    size = image.get_size()
    size = size[0] * scale, size[1] * scale
    image = pygame.transform.scale(image, size)

    return image, image.get_rect()

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

cloud = pygame.image.load("assets/cloud.png")

bird, birdpos = load_image("bird.png", 0.35)
bird_width = bird.get_size()[0]
bird_height = bird.get_size()[1]

birdpos.x, birdpos.y, = (screen.get_width() / 2) - (bird_width / 2), (screen.get_height() / 2) - (bird_height / 2)

while running:
    screen.blit(bird, birdpos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    print(birdpos.y)

    screen.fill("blue")

    birdpos = birdpos.move(bird_speed)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if birdpos.top <= 0:
            birdpos.y += -2
        else:
            birdpos.y += -300 * dt
    elif birdpos.bottom >= height:
        birdpos.y += -2


    screen.blit(bird, birdpos)
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()