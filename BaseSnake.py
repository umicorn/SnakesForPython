import pygame, sys
from random import randint
from pygame.locals import *

# Python Lesssson #1: Introduction to Python
# Snake is one of the earliest video games in video game history.
# You control a snake with the directional arrows (left, right, up, down) and grow as you eat.
# If you bump into a wall or part of yourself, you lose! (Or at least, you should!
# You can learn more about this game here: https://en.wikipedia.org/wiki/Snake_(video_game)

# Comments are preceded by a pound sign (#).
# There will be commented blocks with questions throughout the code.
# These questions come in two flavors:
#     Questions starting with Q X.Y: expect answers. Answer them in comments below them.
#     Questions unmarked may be covered in discussion. Discuss with your partner and be prepared to share
#     your answers with the class.

# You are not expected to read this code from the top-down. Jump around the code. Try to make sense of it.
# Try to change code. Be prepared to share your findings.

# Code preceded by "def" are called functions. They are very similar to methods in Java.
# Q 1.1: How is Java different than Python (try to get at least 5 differences)?
# Q 1.2: In Java, what is a method?
# Q 1.3: How does a Python function look different than a Java method?

# Useful debug method. Text is a string, rect is a Rect.
def printRect(text, rect):
    print text + " Top-left: (" + str(rect.left) + ", " + str(oldPiece.top) + ")"

# Code for if snake runs into itself or game exits.
def quitGame():
    print "Game over!"
    # How can we measure the player's score?
    print "Your score is: "
    sys.exit(0)

# Code to move the head.
def moveHead(headRect, dir):
    if dir == 1:
        deltaX = blockSize
    elif dir == 3:
        deltaX = -blockSize
    else:
        deltaX = 0

    if dir == 0:
        deltaY = blockSize
    elif dir == 2:
        deltaY = -blockSize
    else:
        deltaY = 0

    newRect= headRect.move(deltaX, deltaY)
    return newRect

# Q 1.4 What do you think return means?

# Accepts two Rects as input.
# Move from to to's location.
def moveBody(toRect, fromRect):
    deltaX = toRect.left - fromRect.left
    deltaY = toRect.top - fromRect.top
    return fromRect.move(deltaX, deltaY)

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

    # If we have not eaten, we need to clear the old rectangle.
    if (not hasEaten):
        pygame.draw.rect(screen, (0, 0, 0), oldRect)

    # Draw the apple.
    pygame.draw.rect(screen, (255, 0, 0), appleRect)


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
# The body of the snake is different than the head.
# These brackets indicate that there is a list.
# Informal Question:
body = []

# Set up the rectangle of the apple.
appleRect = randomRect()

# Set up the screen.
pygame.init()
scrHeight = 40 * blockSize
scrWidth = 40 * blockSize
clock = pygame.time.Clock()
screen = pygame.display.set_mode((scrHeight, scrWidth))

# This loop is interesting. When will it stop running?
while True:
    clock.tick(10)

    # Handle keyboard input..
    for ev in pygame.event.get():
        if ev.type == QUIT:
            quitGame()
        # Handle directions. What does the logic say? What will it prevent?
        elif ev.type == KEYDOWN:
            if ev.key == K_UP and (not body or direction != 0):
                direction = 2
            elif ev.key == K_DOWN and (not body or direction != 2):
                direction = 0
            elif ev.key == K_LEFT and (not body or direction != 1):
                direction = 3
            elif ev.key == K_RIGHT and (not body or direction != 3):
                direction = 1
    # Copy the old Rect.
    oldPiece = head.copy()
    # Move the head.
    head = moveHead(head, direction)

    # Update the snake's body (excluding the head).
    for i in range(0, len(body)):
        temp = body[i].copy()
        body[i] = moveBody(oldPiece, body[i])
        oldPiece = temp

    # If the snake collides with itself, end the game.
    # Else, if we eat an apple, generate a new apple and add another block (at oldPiece) to the snake
    hasEaten = head.colliderect(appleRect)
    # Checks if the head collides with pieces in the body.
    if (head.collidelist(body) != -1):
        print "Collided with body"
        # What should we do if a snake crashes into itself?
    # Checks if the head collides with the body.
    if (head.colliderect(appleRect)):
        appleRect = randomRect()
        body.append(oldPiece)
    # How could we keep a snake from going off the screen?

    draw(oldPiece, hasEaten)
    pygame.display.flip()






