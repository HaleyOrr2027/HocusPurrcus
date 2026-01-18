import pygame
from sys import exit
from random import randint

pygame.init()
pygame.display.set_caption('Hocus Purr-cus')
screen = pygame.display.set_mode((800, 533))
clock = pygame.time.Clock()

game_active = True

# Background ----------------------------------------------- 

bg_surface = pygame.image.load("C:/Users/haley/OneDrive/Documents/GitHub/HocusPurrcus/Hocus Purrr-cus/Graphics/background.png").convert_alpha()

# Player  -------------------------------------------------

player_surf = pygame.image.load("C:/Users/haley/OneDrive/Documents/GitHub/HocusPurrcus/Hocus Purrr-cus/Graphics/player.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (400, 533))
player_direction = 0

# Player HP -----------------------------------------------

player_HP0 = pygame.image.load("C:/Users/haley/OneDrive/Documents/GitHub/HocusPurrcus/Hocus Purrr-cus/Graphics/HP.png").convert_alpha()
player_HP0_rect = player_surf.get_rect(center = (300, 200))

# Wizard  -------------------------------------------------

wizard2_surf = pygame.image.load("C:/Users/haley/OneDrive/Documents/GitHub/HocusPurrcus/Hocus Purrr-cus/Graphics/wizard_2.png").convert_alpha()
wizard2_rect = wizard2_surf.get_rect(midbottom = (400, 460))
wizard_wiggle_offset = 0
wizard_wiggle_direction = 0

# Wizard HP -----------------------------------------------

wizard_HP0 = pygame.transform.flip(player_HP0, 1, 0)
wizard_HP0_rect = player_surf.get_rect(center = (740, 200))

# Music ---------------------------------------------------

music = pygame.mixer.Sound("C:/Users/haley/OneDrive/Documents/GitHub/HocusPurrcus/Hocus Purrr-cus/Music/FightMusic.mp3")
music.play(-1)
music.set_volume(0.2)


# Functions -----------------------------------------------

def click_effect():
    global wizard_wiggle_direction, wizard_wiggle_offset


    if wizard_wiggle_direction != 0:
        wizard_wiggle_offset += 2 * wizard_wiggle_direction

    # reverse direction at limits
    if wizard_wiggle_offset >= 8:
        wizard_wiggle_direction = -1
    if wizard_wiggle_offset <= -8:
         wizard_wiggle_direction = 1

    # stop when settled near center
    if abs(wizard_wiggle_offset) < 2 and wizard_wiggle_direction == 1:
        wizard_wiggle_offset = 0
        wizard_wiggle_direction = 0


def player_movement():

    # move a little each frame
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        player_rect.x += 3
    if keys[pygame.K_LEFT]:
        player_rect.x -= 3


    # clamp to bounds and stop
    if player_rect.x <= -50:
        player_rect.x = -50
    if player_rect.x >= 400:
        player_rect.x = 400

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    

        if event.type == pygame.MOUSEBUTTONDOWN and wizard2_rect.collidepoint(event.pos):
            #Start moving the wizard to the right
            wizard_wiggle_direction = 1
        

    if game_active:

        click_effect()
        player_movement()

        screen.blit(bg_surface, (0,0))
        screen.blit(wizard2_surf, (wizard2_rect.x + wizard_wiggle_offset, wizard2_rect.y))
        screen.blit(player_surf, player_rect)
        screen.blit(player_HP0, player_HP0_rect)
        screen.blit(wizard_HP0, wizard_HP0_rect)





    pygame.display.update()
    clock.tick(60)
