import pygame, sys
from random import randint
from pygame.locals import *
from Constants import *

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


walls = []


def initWalls(screen):
    for i in range(0, xBound):
        for j in range(0, yBound):
            walls.append( Rect(i * blockSize, 0, blockSize, blockSize) )
            walls.append( Rect(0, j * blockSize, blockSize, blockSize) )
            walls.append( Rect(i * blockSize, (yBound - 1) * blockSize, blockSize, blockSize) )
            walls.append( Rect((xBound - 1) * blockSize, j * blockSize, blockSize, blockSize) )

    # Draw the walls
    for wall in walls:
        pygame.draw.rect(screen, (0, 0, 255), wall)


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
    return Rect(randint(1, xBound - 2) * blockSize, randint(1, yBound - 2) * blockSize, blockSize, blockSize)

# Draw the screen depending on what happens.
def draw(oldPiece, head, body, appleRect, hasEaten, screen):


    # Draw the head.
    pygame.draw.rect(screen, (0, 255, 0), head)
    # Draw the body.
    for block in body:
        pygame.draw.rect(screen, (0, 155, 0), block)

    # If we have not eaten, we need to clear the old rectangle.
    if (not hasEaten):
        pygame.draw.rect(screen, (0, 0, 0), oldPiece)

    # Draw the apple.
    pygame.draw.rect(screen, (255, 0, 0), appleRect)




