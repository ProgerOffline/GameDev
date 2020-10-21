import pygame
from colors import *
from control import *
from snake import *
from gui import *
from food import *

pygame.init()
screen = pygame.display.set_mode((441, 441))
pygame.display.set_caption("Snake game")

Control = Control()
Snake = Snake()
Gui = Gui()
Food = Food()
Gui.initField()
Food.getFoodPos(Gui)

speed = 10

while Control.flagGame:
	Gui.checkWinOrLose()
	Control.keyPress()

	screen.fill(black)

	if Gui.onGame == "GAME":
		Snake.drawSnake(screen)
		Gui.drawLevel(screen)
		Food.drawFood(screen)
		Gui.drawIndicator(screen)
	elif Gui.onGame == "WIN":
		Gui.drawWin(screen)
	elif Gui.onGame == "LOSE":
		Gui.drawLose(screen)

	if Control.flagPause:
		Snake.move(Control)
		Snake.checkBarrier(Gui)
		Snake.eat(Food, Gui)
		Snake.animation()
		Snake.checkEndWindow()
	else:
		Gui.drawPauseImage(screen)

	pygame.time.Clock().tick(speed)
	pygame.display.flip()