import pygame

def dialogues(text_lines):
    FPS = 144
    pygame.font.init()
    pygame.init()
    font = pygame.font.SysFont(None, 50)

    screen = pygame.display.set_mode((1920/1.3, 1080/2))
    clock = pygame.time.Clock()

    while True:
        
        rect_box = 0

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(10, 10, 1920/1.3-20, 15))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(1920/1.3-35, 15, 1920/1.3-30, 1080/2-20))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(10, 10, 1920/1.3-20, 15))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(10, 10, 1920/1.3-20, 15))


        y_position = 100
        for line in text_lines:
            text_surface = font.render(line, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(screen.get_width() // 2, y_position))
            screen.blit(text_surface, text_rect)
            y_position += 50  

        pygame.display.flip()

text = ["oui", "non", "peut-etre"]
dialogues(text)
