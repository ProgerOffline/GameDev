import pygame
import time
import random
from config import *

pygame.init()
pygame.display.set_caption("Камень, ножницы, бумага")

class StartGame():
    counter = 0

    def __init__(self):
        global USER_INDEX, pcSprites
        self.userIndex = USER_INDEX
        self.sprites = pcSprites

    def chooseWinner(self):
        global PC_INDEX, text

        if USER_INDEX == PC_INDEX:
            text = "Ничья!"
        elif USER_INDEX == 1 and PC_INDEX == 0 or \
             USER_INDEX == 0 and PC_INDEX == 2 or \
             USER_INDEX == 2 and PC_INDEX == 1:
             text = "Вы выиграли!"

        elif USER_INDEX == 0 and PC_INDEX == 1 or \
             USER_INDEX == 1 and PC_INDEX == 2 or \
             USER_INDEX == 2 and PC_INDEX == 0:
             text = "Вы проиграли!"


    def choosePc(self):
        global pcPosX, pcPosY, PC_INDEX
        while self.counter != tiks:
            PC_INDEX += 1
            if PC_INDEX == 3: PC_INDEX = 0

            self.counter += 1

            screen.blit(self.sprites[PC_INDEX], [pcPosX, pcPosY])

            pygame.display.update()


class Changer:
    def addUserIndex(self):
        global USER_INDEX
        global PC_INDEX

        USER_INDEX += 1
        if USER_INDEX == 3: USER_INDEX = 0

    def removeUserIndex(self):
        global USER_INDEX

        if USER_INDEX == -1: USER_INDEX = 2
        USER_INDEX -= 1

    def addPcIndex(self):
        global PC_INDEX

        PC_INDEX += 1
        if PC_INDEX == 3: PC_INDEX = 0

class Draw(Changer):
    def __init__(self):
        global userSprites, pcSprite, pcSprites, playButton, leftArrow, rightArrow

        self.userSprites = userSprites
        self.pcSprites = pcSprites
        self.pcSprite = pcSprite
        self.playButton = playButton
        self.leftArrow = leftArrow
        self.rightArrow = rightArrow

    def drawSprites(self):
        global userPosX, userPosY, pcPosX, pcPosY, leftArrowPosY, leftArrowPosX, rightArrowPosY, rightArrowPosX, playButtonPosX, playButtonPosY

        screen.blit(self.userSprites[USER_INDEX], [userPosX, userPosY])
        screen.blit(self.playButton, [playButtonPosX, playButtonPosY])

        screen.blit(self.leftArrow, [leftArrowPosX, leftArrowPosY])
        screen.blit(self.rightArrow, [rightArrowPosX, rightArrowPosY])

        if PC_INDEX <= -1:
            screen.blit(self.pcSprite, [pcPosX, pcPosY])
        else:
            screen.blit(self.pcSprites[PC_INDEX], [pcPosX, pcPosY])

        self.pcAnimation()

    def drawFont(self, text):
        global RED, GREEN, BLACK
        font = pygame.font.SysFont('couriernew', 48)

        if text == "Вы выиграли!":
            returnText = font.render(text, 1, (GREEN))
        elif text == "Вы проиграли!":
            returnText = font.render(text, 1, (RED))
        else:
            returnText = font.render(text, 1, (BLACK))

        textPlace = returnText.get_rect(center=(410, 30))

        screen.blit(returnText, textPlace)
        pygame.display.update()


    def pcAnimation(self):
        global pcPosY, onGame, counter

        if counter == 4:
            if onGame:
                pcPosY -= 1
            elif not onGame:
                pcPosY += 1

            if pcPosY <= 60:
                onGame = False
            elif pcPosY >= 65:
                onGame = True
            counter = 0

        counter += 1

runGame = True
while runGame:

    mouseX, mouseY = pygame.mouse.get_pos()
    screen.fill((255, 204, 0))

    Draw().drawSprites()
    Draw().drawFont(text)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: runGame = False

    if mouseX > leftArrowPosX and mouseX < leftArrowPosX + leftArrowLenX:
        xInsideLeft = True
    else:
        xInsideLeft = False

    if mouseY > leftArrowPosY and mouseY < leftArrowPosY + leftArrowLenY:
        yInsideLeft = True
    else:
        yInsideLeft = False

    if xInsideLeft and yInsideLeft:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                time.sleep(0.09)
                Changer().removeUserIndex()

    if mouseX > rightArrowPosX and mouseX < rightArrowPosX + rightArrowLenX:
        xInsideRight = True
    else:
        xInsideRight = False

    if mouseY > leftArrowPosY and mouseY < leftArrowPosY + leftArrowLenY:
        yInsideRight = True
    else:
        yInsideRight = False

    if xInsideRight and yInsideRight:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                time.sleep(0.07)
                Changer().addUserIndex()

    if mouseX > playButtonPosX and mouseX < playButtonPosX + playButtonLenX:
        xInsideRightButton = True
    else:
        xInsideRightButton = False

    if mouseY > playButtonPosY and mouseY < playButtonPosY + playButtonLenY:
        yInsideRightButton = True
    else:
        yInsideRightButton = False

    if xInsideRightButton and yInsideRightButton:

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                time.sleep(0.3)
                start = StartGame()
                start.choosePc()
                start.chooseWinner()

    tiks = random.randint(150, 201)
    pygame.time.Clock().tick(65)
    pygame.display.update()

pygame.quit()
