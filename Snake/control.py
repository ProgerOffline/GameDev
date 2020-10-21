import pygame
from pygame.locals import *

class Control:
	def __init__(self):

		self.flagGame = True
		self.flagDirection = "RIGHT"
		self.flagPause = True

	def keyPress(self):
		"""Управление в зависимоси от флага"""
		for event in pygame.event.get():
			if event.type == QUIT:
				self.flagGame = False
			elif event.type == KEYDOWN:
				if event.key == K_RIGHT and self.flagDirection != "LEFT":
					self.flagDirection = "RIGHT"
				elif event.key == K_LEFT and self.flagDirection != "RIGHT":
					self.flagDirection = "LEFT"
				elif event.key == K_UP and self.flagDirection != "DOWN":
					self.flagDirection = "UP"
				elif event.key == K_DOWN and self.flagDirection != "UP":
					self.flagDirection = "DOWN"
				elif event.key == K_ESCAPE:
					self.flagGame = False
				elif event.key == K_SPACE:
					if self.flagPause:
						self.flagPause = False
					elif self.flagPause == False:
						self.flagPause = True

