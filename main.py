import pygame
from pygame.locals import *

window_width, window_height = 800, 600
block_dimension = 50

class Block:
    def __init__(self, image_path, x, y) -> None:
        self.block = pygame.transform.scale(pygame.image.load(image_path), (block_dimension, block_dimension))
        self.x = x
        self.y = y

class Snake:
    def __init__(self) -> None:
        self.head = Block("assets/snake_head.png", 0, 0)

    def updateSnake(self, x, y) -> None:
        self.head.x += x
        self.head.y += y


class SnakeGame:
    def __init__(self) -> None:
        pygame.init()

        self.window = pygame.display.set_mode((window_width, window_height))
        self.window.fill((143,188,143))
        pygame.display.set_caption("Karan's Snake Game")
        pygame.display.set_icon(pygame.image.load('assets/snake_game_logo.png'))

        self.snake = Snake()

        self.moveSnake(0, 0)

        self.running  = True

        while self.running == True:
            self.gamerun()
    
    def gamerun(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running  = False

                if event.key == K_UP:
                    self.moveSnake(0, -block_dimension)
                elif event.key == K_DOWN:
                    self.moveSnake(0, block_dimension)
                elif event.key == K_LEFT:
                    self.moveSnake(-block_dimension, 0)
                elif event.key == K_RIGHT:
                    self.moveSnake(block_dimension, 0)

            if event.type == QUIT:
                self.running  = False


    def moveSnake(self, x, y):
        self.window.fill((143,188,143))
        self.snake.updateSnake(x, y)
        self.window.blit(self.snake.head.block, (self.snake.head.x, self.snake.head.y))
        pygame.display.flip()



if __name__ == "__main__":
    SnakeGame()