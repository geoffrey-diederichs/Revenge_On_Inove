import pygame
from player import Player
from collisionsMap import collision
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

#offset that moves the camera at the load of map
offset = {
    'x': 50.5*tileSize*zoomMapLevel,
    'y': 17*tileSize*zoomMapLevel
}

#1dArray with all collisions
collisionsArray = collision()
#2dArray witl all collisions
collisionsMap = [int]


#Make 1d to 2dArray
for i in range(0, len(collisionsArray), 150):
    collisionsMap.append(collisionsArray[0+i: 151+i])

FPS = 144

#create instance of background class 
background = Background()

#create instance of all collision
for i in range(1, len(collisionsMap), 1):
    for j in range(0, 150, 1):
        if (collisionsMap[i][j] == 126):
            Collision((j)*zoomMapLevel*tileSize-offset['x'], (i-1.3)*zoomMapLevel*tileSize-offset['y'])

text = ["on va tester les dialogues", "oui"]
#.convert_alpha() is very important, without it the game is much laggier
bg = (pygame.image.load(background.imgSrc)).convert_alpha()
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
    global movable
    movable = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        moveX = 1
        for i in allCollisions:
            if (check_collisions('left', i)):
                movable = False
        
    if keys[pygame.K_RIGHT]:
        moveX = -1
        for i in allCollisions:
            if (check_collisions('right', i)):
                movable = False

    if keys[pygame.K_UP]:
        moveY = 1
        for i in allCollisions:
            if (check_collisions('up', i)):
                movable = False

    if keys[pygame.K_DOWN]:
        moveY = -1
        for i in allCollisions:
            if (check_collisions('bottom', i)):
                movable = False

    if keys[pygame.K_e]:
        dialogues(text)

    if movable:
        player.position_y -= moveY
        player.position_x -= moveX
        background.x += moveX
        background.y += moveY
        for i in allCollisions:
            i.y += moveY
            i.x += moveX 

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
    while True:
        #re fill the whole screen therefore makes it refresh each frame
        screen.fill('black')
        #limit frames by 144 atm
        clock.tick(FPS)

        #quit the game if f4
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        #fill the screen with background image at x, y
        screen.blit(bg, (background.x-offset['x'], background.y-offset['y']))
        screen.blit(playerSprite, (width/2, height/2), (player.frameX*zoomMapLevel, player.frameY, player.frameX+player.width*zoomMapLevel, 16*zoomMapLevel))

        player.animate()

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

movable = True
main()
