import pygame
import time
import random

pygame.init()

# Set the display width and height
display_width = 800
display_height = 600

# Set the colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
purple = (0, 0, 128)

# Set the size of each snake block and the speed of the snake
block_size = 20
snake_speed = 15

# Set the font for displaying the score
font = pygame.font.SysFont(None, 25)

# Function to display the score
def display_score(score):
    text = font.render("Score: " + str(score), True, white)
    gameDisplay.blit(text, [0, 0])

# Function to draw the snake
def draw_snake(block_size, snakeList):
    for XnY in snakeList:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])

# Function to display a message
def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width / 6, display_height / 3])

# Set the game display
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

# Clock for controlling the game speed
clock = pygame.time.Clock()

# Function to run the game
def gameLoop():
    gameExit = False
    gameOver = False

    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 0
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX = round(random.randrange(0, display_width - block_size) / block_size) * block_size
    randAppleY = round(random.randrange(0, display_height - block_size) / block_size) * block_size

    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(purple)
            message_to_screen("Game Over! Press C to play again or Q to quit", red)
            display_score(snakeLength - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(purple)
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, block_size, block_size])

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        draw_snake(block_size, snakeList)
        display_score(snakeLength - 1)

        pygame.display.update()

        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = round(random.randrange(0, display_width - block_size) / block_size) * block_size
            randAppleY = round(random.randrange(0, display_height - block_size) / block_size) * block_size
            snakeLength += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
