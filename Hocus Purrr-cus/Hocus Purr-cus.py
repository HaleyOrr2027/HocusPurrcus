import pygame
from sys import exit
from random import randint

pygame.init()
pygame.display.set_caption('Hocus Purr-cus')
screen = pygame.display.set_mode((800, 533))
clock = pygame.time.Clock()

# Background ----------------------------------------------- 

bg_surface = pygame.image.load("C:/Users/haley/OneDrive/Documents/GitHub/HocusPurrcus/Hocus Purrr-cus/Graphics/background.png").convert_alpha()

# Player  -------------------------------------------------

player_surf = pygame.image.load("C:/Users/haley/OneDrive/Documents/GitHub/HocusPurrcus/Hocus Purrr-cus/Graphics/player.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (400, 533))

# Player HP -----------------------------------------------

player_HP0 = pygame.image.load("C:/Users/haley/OneDrive/Documents/GitHub/HocusPurrcus/Hocus Purrr-cus/Graphics/HP.png").convert_alpha()
player_HP0_rect = player_surf.get_rect(center = (300, 200))

# Wizard  -------------------------------------------------

wizard2_surf = pygame.image.load("C:/Users/haley/OneDrive/Documents/GitHub/HocusPurrcus/Hocus Purrr-cus/Graphics/wizard_2.png").convert_alpha()
wizard2_rect = wizard2_surf.get_rect(midbottom = (400, 460))

# Wizard HP -----------------------------------------------

wizard_HP0 = pygame.transform.flip(player_HP0, 1, 0)
wizard_HP0_rect = player_surf.get_rect(center = (740, 200))

# Music ---------------------------------------------------

music = pygame.mixer.Sound("C:/Users/haley/OneDrive/Documents/GitHub/HocusPurrcus/Hocus Purrr-cus/Music/FightMusic.mp3")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(bg_surface, (0,0))
    screen.blit(wizard2_surf, wizard2_rect)
    screen.blit(player_surf, player_rect)
    screen.blit(player_HP0, player_HP0_rect)
    screen.blit(wizard_HP0, wizard_HP0_rect)
    music.play()
    music.set_volume(0.2)


    pygame.display.update()
    clock.tick(60)
