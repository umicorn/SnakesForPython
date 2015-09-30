import pygame, sys
from random import randint
from pygame.locals import *

# Code for if snake runs into itself or game exits.
def quitGame():
    sys.exit(0)

def moveHead(headRect, dir):
    if dir == 1:
        deltaX = blockSize
    elif dir == 3:
        deltaX = blockSize
    else:
        deltaX = 0

    if dir == 0:
        deltaY = -blockSize
    elif dir == 2:
        deltaY = blockSize
    else:
        deltaY = 0
    headRect.move(deltaX, deltaY)
    return headRect

# Accepts two Rects as input.
# Move from to to's location.
def moveBody(toRect, fromRect):
    deltaX = toRect.left - fromRect.left
    deltaY = toRect.top - fromRect.top
    fromRect.move(deltaX, deltaY)

# Creates a random rectangle.
def randomRect():
    return Rect(randint(0, xBound) * blockSize, randint(0,yBound) * blockSize, blockSize, blockSize)

# Draw the screen depending on what happens.
def draw(oldRect, hasEaten):
    # Draw the head.
    pygame.draw.rect(screen, (0, 255, 0), head)
    # Draw the body.
    for block in body:
        pygame.draw.rect(screen, (0, 155, 0), block)
    pygame.draw.rect(screen, (255, 0, 0), appleRect)

    # If we have not eaten, we need to clear the old rectangle.
    if (not hasEaten):
        pygame.draw.rect(screen, (0, 0, 0), oldRect)


# Direction traveled is encoded as an integer.
# 0 - DOWN | 1 - RIGHT | 2 - UP | 3 - LEFT
direction = 0

# The size of a single block
blockSize = 20
# The maximum number of blocks on each side.
xBound = 20
yBound = 20

# The head and body of the snake.
head = Rect(20 * blockSize, 20 * blockSize, blockSize, blockSize)
# The body of the snake does not contain the head.
body = []

# Set up the rectangle of the apple.
appleRect = randomRect()

# How much food eaten.
score = 0

# Set up the screen
pygame.init()
scrHeight = 40 * blockSize
scrWidth = 40 * blockSize
clock = pygame.time.Clock()
screen = pygame.display.set_mode((scrHeight, scrWidth))

# This loop is interesting. When will it stop running?
while True:
    clock.tick(10)
    # Handle keyboard input. Please do not touch this logic.
    for ev in pygame.event.get():
        if ev.type == QUIT:
            quitGame()
        # Handle directions. What does the logic say? What will it prevent?
        elif ev.type == KEYDOWN:
            if ev.key == K_UP and direction != 0:
                direction = 2
            elif ev.key == K_DOWN and direction != 2:
                direction = 0
            elif ev.key == K_LEFT and direction != 1:
                direction = 3
            elif ev.key == K_RIGHT and direction != 3:
                direction = 1
    # Copy the old Rect.
    oldPiece = head.copy()
    # Move the head.
    head = moveHead(head, direction)

    # Update the snake's body (excluding the head).
    for i in range(0, len(body)):
        temp = body[i].copy()
        moveBody(oldPiece, body[i])
        oldPiece = temp

    # If the snake collides with itself, end the game.
    # Else, if we eat an apple, generate a new apple and add another block (at oldPiece) to the snake
    hasEaten = head.colliderect(appleRect)
    if (head.collidelist(body)):
        print "Collided with body"
        quitGame()
    if (head.colliderect(appleRect)):
        appleRect = randomRect()
        body.append(oldPiece)

    draw(oldPiece, hasEaten)






