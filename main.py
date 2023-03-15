import pygame
from pygame.locals import *

window_width, window_height = 800, 600
block_dimension = 50

def addBlock(image_path):
    return pygame.transform.scale(pygame.image.load(image_path), (block_dimension, block_dimension))

def buildBlock(block, x, y):
    window.fill((143,188,143))
    window.blit(block, (x, y))
    pygame.display.flip()


pygame.init()

window = pygame.display.set_mode((window_width, window_height))
window.fill((143,188,143))
pygame.display.set_caption("Karan's Snake Game")
pygame.display.set_icon(pygame.image.load('assets/snake_game_logo.png'))

head = addBlock("assets/snake_head.png")
head_x, head_y = 0, 0
window.blit(head, (head_x, head_y ))

pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_UP:
                head_y -= block_dimension
                buildBlock(head, head_x, head_y)
            elif event.key == K_DOWN:
                head_y += block_dimension
                buildBlock(head, head_x, head_y)
            elif event.key == K_LEFT:
                head_x -= block_dimension
                buildBlock(head, head_x, head_y)
            elif event.key == K_RIGHT:
                head_x += block_dimension
                buildBlock(head, head_x, head_y)



        if event.type == QUIT:
            running = False