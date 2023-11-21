import pygame

FPS = 144
screen = pygame.display.set_mode((1920, 1080))
height = screen.get_height()
width = screen.get_width()

def dialogues(text_lines, screen):
    pygame.font.init()
    font = pygame.font.SysFont(None, 50)

    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(width-width+300, height/2+200, width-590, height-760))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(width-width+315, height/2+215, width-620, height-790))

    y_position = 800
    for line in text_lines:
        text_surface = font.render(line, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(screen.get_width() // 2, y_position))
        screen.blit(text_surface, text_rect)
        y_position += 50


def main():
    pygame.init()
    bg = pygame.image.load("C:/Users/alexa/Documents/ynov/fighting-game/img/maps/map1.png")
    bg_size = bg.get_size()
    background_pos = pygame.Vector2(width / 2, height / 2)
    player_pos = pygame.Vector2(width / 2, height / 2)
    
    offset = {
        'x': width / 2,
        'y': height / 2
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
            background_pos.x += 5
        if keys[pygame.K_RIGHT]:
            background_pos.x -= 5
        if keys[pygame.K_UP]:
            background_pos.y += 5
        if keys[pygame.K_DOWN]:
            background_pos.y -= 5

        screen.blit(bg, background_pos)
        pygame.draw.circle(screen, "red", player_pos, 20)
        text = ["on va tester les dialogues", "oui"]
        dialogues(text, screen)

        pygame.display.flip()


main()
