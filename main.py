import sys, pygame, random, os, math, time
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
        self.rect.x, self.rect.y = (width / 2) - (self.image.get_size()[0] / 2), (screen.get_height() / 2) - (self.image.get_size()[1] / 2)
        self.area = self.rect
        self.mask = pygame.mask.from_surface(self.image)

    def up(self):
        self.rect.y += -300 * dt

    def update(self):
        if self.rect.topleft[1] >= height:
            self.kill()

class Pipe(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("pipes.png", 0.4)
        self.rect.x, self.rect.y = width, random.uniform(-550, -320)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect = self.rect.move(-3, 0)
        if self.rect.x <= -self.image.get_width() - 10:
            self.kill()





main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "assets")

size = width, height = 1000, 600
bird_speed = [0, 2.8]
pygame.display.set_caption("PyBird")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
dt = 0

regfont = pygame.font.Font("assets/pixeloidbold.ttf", 64)
smallerfont = pygame.font.Font("assets/pixeloid.ttf", 48)
tinyfont = pygame.font.Font("assets/pixeloid"".ttf", 32)

losttxt = regfont.render("You've lost!", True, "crimson")
textpos = (width / 2 - losttxt.get_width() / 2, height / 2 - losttxt.get_height() / 2)

againtxt = smallerfont.render("Play again?", True, "crimson")
againpos = (width / 2 - againtxt.get_width() / 2, height / 2 + losttxt.get_height() - 35)

yestxt = tinyfont.render("Yes", True, "Crimson")
yespos = (againtxt.get_width() / 2, height / 2 + againtxt.get_height() + 45)

bg = pygame.image.load("assets/background.png")

bg = pygame.transform.scale(bg, (1100, 600))
scroll_x = 0
bg_x = 0


pipes = pygame.sprite.Group()

pipe = Pipe()
pipes.add(pipe)

kaboom, kaboompos = load_image("kaboom.png", 0.12)

bird = Bird()

NEWPIPE = pygame.USEREVENT

pygame.display.set_icon(bird.image)

pygame.time.set_timer(NEWPIPE, 2000)

lost = False

while running:
    screen.blit(bird.image, bird.rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == NEWPIPE:
            pipe = Pipe()
            pipes.add(pipe)






    screen.blit(bg, (scroll_x, 0))
    screen.blit(bg, (bg_x + width, 0))




    if scroll_x <= -width:
        scroll_x = 0

    if bg_x <= -width:
        bg_x = 0

    if not lost:
        if pygame.mouse.get_visible() == True:
            pygame.mouse.set_visible(False)
        collisionpoint = None
        for x in pipes:
            collisionpoint = pygame.sprite.collide_mask(bird, x)
            if collisionpoint != None:
                kaboompos = bird.rect.topleft
                lost = True

        pipes.update()
        scroll_x -= 1
        bg_x -= 1

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            if bird.rect.top <= 0:
                bird.rect.y += -2
                kaboompos = bird.rect.topleft
                lost = True
            else:
                bird.up()
        elif bird.rect.bottom >= height:
            kaboompos = bird.rect.topleft
            lost = True
            bird.rect.y += -2


    pipes.draw(screen)

    bird.rect = bird.rect.move(bird_speed)

    bird.update()
    screen.blit(bird.image, bird.rect)

    if lost:
        screen.blit(kaboom, kaboompos)
        screen.blit(losttxt, textpos)
        screen.blit(againtxt, againpos)
        screen.blit(yestxt, yespos)
        if pygame.mouse.get_visible() == False:
            pygame.mouse.set_visible(True)

    pygame.display.flip()
    pygame.display.update()

    dt = clock.tick(60) / 1000

pygame.quit()