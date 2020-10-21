import pygame
import random

screen = pygame.display.set_mode((800, 400))

userSprites = [ pygame.image.load("images/rock.png"),
                pygame.image.load("images/papper.png"),
                pygame.image.load("images/scissors.png")]

pcSprites = [   pygame.image.load("images/rock.png"),
                pygame.image.load("images/papper.png"),
                pygame.image.load("images/scissors.png")]

pcSprite = pygame.image.load("images/pc_icon.png")


leftArrow = pygame.image.load("images/left_arrow.png")
rightArrow = pygame.image.load("images/right_arrow.png")

leftArrowLenX = leftArrow.get_width()
leftArrowLenY = leftArrow.get_height()

rightArrowLenX = rightArrow.get_width()
rightArrowLenY = rightArrow.get_height()

leftArrowPosX = 135
leftArrowPosY = 310

rightArrowPosX = 195
rightArrowPosY = 310


playButton = pygame.image.load("images/play_button.png")

playButtonLenX = playButton.get_width()
playButtonLenY = playButton.get_height()

playButtonPosX = 310
playButtonPosY = 300

USER_INDEX = 0
PC_INDEX = -1

userPosX = 100
userPosY = 60

pcPosX = 500
pcPosY = 60

onGame = True
counter = 0

text = ""

RED = (188, 19, 57)
GREEN = (0, 180, 0)
BLACK = (0, 0, 0)
