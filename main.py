import pygame
from pygame.locals import *
import random
window_width, window_height = 500, 500
block_dimension = 50

class Block:
    def __init__(self, image_path, x, y) -> None:
        self.block = pygame.transform.scale(pygame.image.load(image_path), (block_dimension, block_dimension))
        self.x = x
        self.y = y

class Food:
    def __init__(self) -> None:
        self.x = random.randint(0, 9) * block_dimension
        self.y = random.randint(0, 9) * block_dimension
        self.block = Block("assets/rat_food.png", self.x, self.y)
        
    def getPosition(self):
        return self.x, self.y
food = Food()

class Snake:
    def __init__(self) -> None:
        self.head = Block("assets/snake_head.png", 0, 0)
        self.body = []

    def updateSnakePosition(self, x, y) -> None:
        if self.body:
            self.body.insert(0, self.body.pop())
            self.body[0].x = self.head.x
            self.body[0].y = self.head.y
        self.head.x += x
        self.head.y += y

    def addSnakeBlock(self) -> None:
        if self.body:
            self.body.append(Block("assets/peach_body.png", self.body[-1].x, self.body[-1].y))
        else:
            self.body.append(Block("assets/peach_body.png", self.head.x, self.head.y))


class SnakeGame:
    def __init__(self) -> None:
        self.score = 0
        pygame.init()

        self.window = pygame.display.set_mode((window_width, window_height))
        self.window.fill((143,188,143))
        pygame.display.set_caption("Karan's Snake Game")
        pygame.display.set_icon(pygame.image.load('assets/snake_game_logo.png'))

        self.food = Food()

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
        self.snake.updateSnakePosition(x, y)
        self.buildSnake()
        print(self.snake.head.x, self.food.block.x, self.snake.head.y, self.food.block.y)
        if ((self.snake.head.x == self.food.block.x) and (self.snake.head.y == self.food.block.y)):
            self.food = Food()
            self.score+=1
            self.snake.addSnakeBlock()
            self.buildSnake()
        pygame.display.flip()

    def buildSnake(self):
        self.window.blit(self.snake.head.block, (self.snake.head.x, self.snake.head.y))

        self.window.blit(self.food.block.block, (self.food.block.x, self.food.block.y))

        for block in self.snake.body:
            self.window.blit(block.block, (block.x, block.y))




if __name__ == "__main__":
    SnakeGame()