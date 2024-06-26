import sys, pygame
pygame.init()

size = width, height = 1000, 600
speed = [0, 2]

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
dt = 0
bird = pygame.image.load("bird.png")
bird = pygame.transform.scale(bird, (200, 200))
birdpos = bird.get_rect()

bdf = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    screen.blit(bird, (bird_pos))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("blue")

    birdrect = birdrect.move(speed)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        birdpos.y += -300 * dt

    screen.blit(bird, birdpos)
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()