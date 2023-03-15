import pygame
from pygame.locals import *

window_width, window_height = 800, 600
block_dimension = 50
head_x, head_y = 0, 0


class Snake:
    def __init__(self) -> None:
        self.head = self.addBlock("assets/snake_head.png")

        self.head_x, self.head_y = 0, 0

    def addBlock(self, image_path):
        return pygame.transform.scale(pygame.image.load(image_path), (block_dimension, block_dimension))



class SnakeGame:
    def __init__(self) -> None:
        pygame.init()

        self.window = pygame.display.set_mode((window_width, window_height))
        self.window.fill((143,188,143))
        pygame.display.set_caption("Karan's Snake Game")
        pygame.display.set_icon(pygame.image.load('assets/snake_game_logo.png'))

        self.snake = Snake()

        self.buildBlock(self.snake.head, self.snake.head_x, self.snake.head_y)

        self.running  = True

        while self.running == True:
            self.gamerun()
    
    def gamerun(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running  = False

                if event.key == K_UP:
                    self.snake.head_y -= block_dimension
                    self.buildBlock(self.snake.head, self.snake.head_x, self.snake.head_y)
                elif event.key == K_DOWN:
                    self.snake.head_y += block_dimension
                    self.buildBlock(self.snake.head, self.snake.head_x, self.snake.head_y)
                elif event.key == K_LEFT:
                    self.snake.head_x -= block_dimension
                    self.buildBlock(self.snake.head, self.snake.head_x, self.snake.head_y)
                elif event.key == K_RIGHT:
                    self.snake.head_x += block_dimension
                    self.buildBlock(self.snake.head, self.snake.head_x, self.snake.head_y)

            if event.type == QUIT:
                self.running  = False


    def buildBlock(self, block, x, y):
        self.window.fill((143,188,143))
        self.window.blit(block, (x, y))
        pygame.display.flip()


running = True

if __name__ == "__main__":
    SnakeGame()