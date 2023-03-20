import pygame
from pygame.locals import *
import random
import time
window_width, window_height = 500, 520
padding = 20
block_dimension = 25

#music
pygame.mixer.init()
pygame.mixer.music.load("assets/pygame_music.mp3")
pygame.mixer.music.play(-1)

class GameBlock:
    def __init__(self, x, y, width, height, color) -> None:
        self.x = x
        self.y = y
        self.block = pygame.Surface((width, height))
        self.block.fill(pygame.Color(color))

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
            self.body.append(Block("assets/peach_body.png", self.head.x-block_dimension, self.head.y-block_dimension))


class SnakeGame:
    def __init__(self) -> None:
        self.score = 0
        pygame.init()

        self.window = pygame.display.set_mode((window_width, window_height))
        self.window.fill((143,188,143))
        pygame.display.set_caption("Karan's Snake Game")
        pygame.display.set_icon(pygame.image.load('assets/snake_game_logo.png'))

        self.footer = GameBlock(0, window_width, window_height-padding, padding, "White")

        self.food = Food()

        self.snake = Snake()

        self.moveSnake(0, 0)

        self.direction = 1

        self.running  = True
        self.lastmove = time.time()
        while self.running == True:
            self.gamerun()

        #Score Screen
        overlay = pygame.Surface((window_width, window_height), pygame.SRCALPHA)
        overlay.fill((128, 128, 128, 128))

        score_text = pygame.font.SysFont(None, 64).render(f"Score: {self.score}", True, (255, 255, 255))

        self.window.blit(overlay, (0, 0))
        self.window.blit(score_text, (window_width / 2 - score_text.get_width() / 2, window_height / 2 - score_text.get_height() / 2))
        pygame.display.update()

        time.sleep(1)


    
    def gamerun(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running  = False

                if event.key == K_UP:
                    if (self.direction != 1):
                        self.moveSnake(0, -block_dimension)
                        self.direction = 0
                elif event.key == K_DOWN:
                    if (self.direction != 0):
                        self.moveSnake(0, block_dimension)
                        self.direction = 1
                elif event.key == K_LEFT:
                    if (self.direction != 3):
                        self.moveSnake(-block_dimension, 0)
                        self.direction = 2
                elif event.key == K_RIGHT:
                    if (self.direction != 2):
                        self.moveSnake(block_dimension, 0)
                        self.direction = 3

            if event.type == QUIT:
                self.running  = False

        if(time.time()-self.lastmove > 0.25):
            if (self.direction == 0):
                self.moveSnake(0, -block_dimension)
            elif (self.direction == 1):
                self.moveSnake(0, block_dimension)
            elif (self.direction == 2):
                self.moveSnake(-block_dimension, 0)
            elif (self.direction == 3):
                self.moveSnake(block_dimension, 0)
            
            self.lastmove = time.time()
    
        if(self.snake.head.x > window_width or self.snake.head.x < 0 or self.snake.head.y > window_height-padding or self.snake.head.y < 0):
            self.running = False

        for body_block in self.snake.body:
            if self.snake.head.x == body_block.x and self.snake.head.y == body_block.y:
                self.running = False



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
        gridSize = 25
        gridColor = pygame.Color("Black")
        for x in range(0, window_width, gridSize):
            pygame.draw.line(self.window, gridColor, (x, 0), (x, window_height))
        for y in range(0, window_height, gridSize):
            pygame.draw.line(self.window, gridColor, (0, y), (window_width, y))

        
        self.window.blit(self.snake.head.block, (self.snake.head.x, self.snake.head.y))

        self.window.blit(self.footer.block, (self.footer.x, self.footer.y))

        score_text = pygame.font.SysFont(None, 30).render(f"Score: {self.score}", True, (0,0,0))
        self.window.blit(score_text, (5, 500))

        self.window.blit(self.food.block.block, (self.food.block.x, self.food.block.y))

        for block in self.snake.body:
            self.window.blit(block.block, (block.x, block.y))
        


if __name__ == "__main__":
    SnakeGame()