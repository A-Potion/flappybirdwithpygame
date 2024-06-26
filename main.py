import sys, pygame, random, os, math
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
        self.rect.x, self.rect.y = (width / 2) - (height / 2), (screen.get_height() / 2) - (self.image.get_size()[1] / 2)
        self.area = self.rect

    def up(self):
        self.rect.y += -300 * dt

class Pipe(pygame.sprite.Sprite):

    def __init__(self):
        self.image, self.rect = load_image("pipe.png", 0.4)
        self.rect.x, self.rect.y = -width, random.uniform(550, 320)


main_dir = os.path.split(os.path.abspath(__file__))[0]
print(main_dir)
data_dir = os.path.join(main_dir, "assets")

size = width, height = 1000, 600
bird_speed = [0, 2]

pygame.display.set_caption("PyBird")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
dt = 0

bg = pygame.image.load("assets/background.png")

bg = pygame.transform.scale(bg, (1100, 600))
scroll_x = 0
bg_x = 0

pipe = Pipe()

pipes = pygame.sprite.Group()
pipes.add(pipe)

bird = Bird()

pygame.display.set_icon(bird.image)

while running:
    screen.blit(bird.image, bird.rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    scroll_x -= 1
    bg_x -= 1

    screen.blit(bg, (scroll_x, 0))
    screen.blit(bg, (bg_x + width, 0))

    if scroll_x <= -width:
        scroll_x = width

    if bg_x <= -width:
        bg_x = width


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

    pygame.display.flip()
    pygame.display.update()

    dt = clock.tick(60) / 1000

pygame.quit()