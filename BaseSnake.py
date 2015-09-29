import pygame
from random import randint
from pygame.locals import *

# Checks for whether or not two rectangles overlap.
def isCollision(rect1, rect2):
    return (not rect1.colliderect(rect2)) and (not rect2.colliderect(rect1))

# Accepts two Rects as input.
# Move from to to's location.
def move(toRect, fromRect):
    deltaX = toRect.left - fromRect.left
    deltaY = toRect.top - fromRect.top
    fromRect.move(deltaX, deltaY)

# Direction traveled is encoded as an integer.
# 0 - DOWN | 1 - RIGHT | 2 - UP | 3 - LEFT
direction = 0

# The size of a single block
blockSize = 20  

# The head and body of the snake.
head = Rect(20 * blockSize, 20 * blockSize, blockSize, blockSize)
body = []

# Set up the rectangle of the apple.
appleRect = Rect(randint(0, 19) * blockSize, randint(0, 19) * blockSize)

# How much food eaten.
score = 0

# Set up the screen
pygame.init()
scrHeight = 40 * blockSize
scrWidth = 40 * blockSize
clock = pygame.time.Clock()
screen=pygame.display.set_mode((scrHeight, scrWidth))

