import pygame

FPS = 144
screen = pygame.display.set_mode((1920, 1080))
bg = pygame.image.load('/home/abel/Pictures/img100.jpg')
bg_size = bg.get_size()
background_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

offset = {
    'x': screen.get_width()/2,
    'y': screen.get_height()/2
}

clock = pygame.time.Clock()
background_pos.x -= offset['x']
background_pos.y -= offset['y']

while True:
    screen.fill('black')
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        background_pos.x += 3
    if keys[pygame.K_RIGHT]:
        background_pos.x -= 3
    if keys[pygame.K_UP]:
        background_pos.y += 3
    if keys[pygame.K_DOWN]:
        background_pos.y -= 3


    screen.blit(bg, background_pos)
    pygame.draw.circle(screen, "red", player_pos, 20)
    pygame.display.flip()

