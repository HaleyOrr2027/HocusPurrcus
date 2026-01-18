import pygame
from sys import exit

pygame.init()
pygame.display.set_caption('Hocus Purr-cus')
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Background ----------------------------------------------

bg_surface = pygame.image.load('Hocus Purrr-cus\Graphics\background.png').convert_alpha()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(bg_surface, screen)
    pygame.display.update()
    clock.tick(60)
