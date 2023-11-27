import pygame
from player import Player
from collisionsMap import * 
from collision import * 
from background import *

pygame.init()
pygame.display.set_caption("revenge on inove")

screen = pygame.display.set_mode((1920, 1080))
height = screen.get_height()
width = screen.get_width()

#size of each tile
tileSize = 16
#the zoomlevel exported from tiled
zoomMapLevel = 4
bg = ""
background = Background()

FPS = 144

text = ["on va tester les dialogues", "oui"]
#.convert_alpha() is very important, without it the game is much laggier
player = Player(width/2, height/2)
playerSprite = (pygame.image.load(player.imgSrc)).convert_alpha()
playerSprite_rect = playerSprite.get_rect()
playerSprite = pygame.transform.scale(playerSprite, (playerSprite_rect.width*zoomMapLevel, playerSprite_rect.height*zoomMapLevel))

def dialogues(text_lines):
    pygame.font.init()
    font = pygame.font.SysFont(None, 55)

    #draw the white outter line from dialogue
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(width-width/1.17, height-height/3.2, width-width/3.4, height-height/1.3))
    #draw the black inner line
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(width-width/1.178, height-height/3.31, width-width/3.26, height-height/1.265))
    #draw the character face
    pygame.draw.rect(screen, "green", pygame.Rect(width-width/1.19, height-height/3.44, width-width/1.1, height-height/1.2))

    text_y_position = width-width/1.67 
    #allow to have multiple lines of dialogue
    for line in text_lines:
        text_surface = font.render(line, True, (255, 255, 255))
        text_rect = (width-width/1.35, text_y_position)
        screen.blit(text_surface, text_rect)
        text_y_position += width-width/1.02

def info():
    #display all the info at the top of the screen
    pygame.font.init()
    font = pygame.font.SysFont(None, 50)
    text_info = "Press e to show dialogue, arrows to move"
    text_surface = font.render(text_info, True, (255, 255, 255))
    text_rect = (0, 0)
    screen.blit(text_surface, text_rect)

def move():
    moveX = 0
    moveY = 0
    global pressed_l
    global pressed_r
    global pressed_u
    global pressed_d
    global movable
    global before_last_key
    global last_key
    movable = True
    tmp_key = last_key
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        last_key = 'left'
        pressed_l = True
        moveX = 1
        for i in allCollisions:
            if (check_collisions('left', i)):
                movable = False
    else:
        pressed_l = False
        
    if keys[pygame.K_RIGHT]:
        last_key = 'right'
        pressed_r = True
        moveX = -1
        for i in allCollisions:
            if (check_collisions('right', i)):
                movable = False
    else:
        pressed_r = False

    if keys[pygame.K_UP]:
        last_key = 'up'
        pressed_u = True
        moveY = 1
        for i in allCollisions:
            if (check_collisions('up', i)):
                movable = False
    else:
        pressed_u = False

    if keys[pygame.K_DOWN]:
        last_key = 'down'
        pressed_d = True
        moveY = -1
        for i in allCollisions:
            if (check_collisions('bottom', i)):
                movable = False
    else:
        pressed_d = False

    if keys[pygame.K_e]:
        dialogues(text)
    if keys[pygame.K_TAB]:
        floor_selection()

    if movable:
        player.position_y -= moveY
        player.position_x -= moveX
        background.x += moveX
        background.y += moveY
        for i in allCollisions:
            i.y += moveY
            i.x += moveX 

    if (tmp_key != last_key):
        before_last_key = tmp_key 

def check_collisions(direction: str, collision: Collision):
    if direction == 'left':
        if (player.position_x-3*tileSize <= collision.fixedX+collision.size and
            player.position_x + player.width >= collision.fixedX and
            player.position_y + player.height + 20 >= collision.fixedY and
            player.position_y - 20 <= collision.fixedY + collision.size):
            return True
    elif direction == 'right':
        if (player.position_x <= collision.fixedX+collision.size and
            player.position_x + player.width+3*tileSize >= collision.fixedX and
            player.position_y + player.height + 20 >= collision.fixedY and
            player.position_y - 20 <= collision.fixedY + collision.size):
            return True
    elif direction == 'up':
        if (player.position_x - 20 <= collision.fixedX+collision.size and
            player.position_x + player.width + 20 >= collision.fixedX and
            player.position_y + player.height>= collision.fixedY and
            player.position_y -3*tileSize<= collision.fixedY + collision.size):
            return True
    elif direction == 'bottom':
        if (player.position_x - 20 <= collision.fixedX+collision.size and
            player.position_x + player.width + 20 >= collision.fixedX and
            player.position_y + player.height +3*tileSize>= collision.fixedY and
            player.position_y<= collision.fixedY + collision.size):
            return True
    return False 

def main():
    clock = pygame.time.Clock()
    load_map("img/floor0.png")
    while True:
        #load_map()
        #re fill the whole screen therefore makes it refresh every frame
        screen.fill('black')
        #limit frames by 144 atm
        clock.tick(FPS)

        #quit the game if f4
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        if last_key == 'left':
            player.frameX = 6*16
            player.animate(pressed_l)
        if last_key == 'right':
            player.frameX = 2*16
            player.animate(pressed_r)
        if last_key == 'up':
            player.frameX = 0*16
            player.animate(pressed_u)
        if last_key == 'down':
            player.frameX = 4*16
            player.animate(pressed_d)

        #fill the screen with background image at x, y
        screen.blit(bg, (background.x-background.offset['x'], background.y-background.offset['y']))
        screen.blit(playerSprite, (width/2, height/2), (player.frameX*zoomMapLevel, player.frameY*zoomMapLevel, player.width*zoomMapLevel, player.height*zoomMapLevel))
        #draw the player (just a red circle atm)
        #pygame.draw.circle(screen, "green", player_pos, 20)

        #draw every collision
        #for i in allCollisions:
            #print(i.fixedX, i.fixedY, player.position_x, player.position_y)
            #pygame.draw.circle(screen, "red", (i.x,i.y), 16)
            #pass

        #display info text
        info()
        #get inputs and move the char
        move()

        #apply all the blit
        pygame.display.flip()

def load_map(imgSrc):
    global bg

    background.imgSrc = imgSrc 
    bg = (pygame.image.load(background.imgSrc)).convert_alpha()

    if background.current_floor == 0:
        collisionsArray = collision_floor0()
        background.offset = {
            'x': 55.5*tileSize*zoomMapLevel,
            'y': 50*tileSize*zoomMapLevel
        }
    elif background.current_floor == 1:
        collisionsArray = collision_floor1()
        background.offset = {
            'x': 0*tileSize*zoomMapLevel,
            'y': 10*tileSize*zoomMapLevel
        }
    else:
        collisionsArray = []


    #2dArray witl all collisions
    collisionsMap = [int]

    #Make 1d to 2dArray
    for i in range(0, len(collisionsArray), 150):
        collisionsMap.append(collisionsArray[0+i: 151+i])

    #create instance of all collision
    for i in range(1, len(collisionsMap), 1):
        for j in range(0, 150, 1):
            if (collisionsMap[i][j] == 126):
                Collision((j)*zoomMapLevel*tileSize-background.offset['x'], (i-1.3)*zoomMapLevel*tileSize-background.offset['y'])

def floor_selection():
    keys2 = pygame.key.get_pressed()
    if background.current_floor == 0:
        text = ["Quel étage ?", "     > RDC", "        1", "        2"]
        if keys2[pygame.K_1]:
            load_map("img/floor1.png")
            background.current_floor = 1
        elif keys2[pygame.K_2]:
            load_map("img/floor2.png")
            background.current_floor = 2
    elif background.current_floor == 1:
        text = ["Quel étage ?", "        RDC", "     > 1", "        2"]
        if keys2[pygame.K_0]:
            load_map("img/floor0.png")
            background.current_floor = 0
        elif keys2[pygame.K_2]:
            load_map("img/floor2.png")
            background.current_floor = 2
    elif background.current_floor == 2:
        text = ["Quel étage ?", "        RDC", "        1", "     > 2"]
        if keys2[pygame.K_0]:
            load_map("img/floor0.png")
            background.current_floor = 0
        elif keys2[pygame.K_2]:
            load_map("img/floor2.png")
            background.current_floor = 2

    text_y_position = width-width/1.28
    pygame.font.init()
    font = pygame.font.SysFont(None, 45)
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(width-width/2.95, height-height/1.58, width-width/1.218, height-height/1.22))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(width-width/3, height-height/1.6, width-width/1.2, height-height/1.194))

    for line in text:
        text_surface = font.render(line, True, (255, 255, 255))
        text_rect = (width-width/3.1, text_y_position)
        screen.blit(text_surface, text_rect)
        text_y_position += width-width/1.02

movable = True
last_key = ""
before_last_key = ""
pressed_l = False
pressed_r = False
pressed_u = False
pressed_d = False
main()
