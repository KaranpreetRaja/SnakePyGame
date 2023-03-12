import pygame
from pygame.locals import *

pygame.init()
width, height = 800, 600

window = pygame.display.set_mode((width, height))
window.fill((143,188,143))
pygame.display.set_caption("Karan's Snake Game")


pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            pass

        if event.type == pygame.QUIT:
            running = False