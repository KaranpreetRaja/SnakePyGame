import pygame
from pygame.locals import *

window_width, window_height = 800, 600


def addblock(image_path):
    block_width, block_height = 100, 100
    return pygame.transform.scale(pygame.image.load(image_path), (block_width, block_height))


pygame.init()

window = pygame.display.set_mode((window_width, window_height))
window.fill((143,188,143))
pygame.display.set_caption("Karan's Snake Game")
pygame.display.set_icon(pygame.image.load('assets/snake_game_logo.png'))

block = addblock("assets/snake_head.png")
window.blit(block, (0, 0))

pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            pass

        if event.type == pygame.QUIT:
            running = False