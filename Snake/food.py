import pygame
import random
from colors import *

class Food:
	def __init__(self):

		self.foodPos = []

	def getFoodPos(self, gui):
		"""Случайно распологает еду на поле""" 

		self.foodPos = random.choice(gui.field)

	def drawFood(self, screen):
		"""Отрисовка еды"""
		pygame.draw.rect(screen, red, pygame.Rect(self.foodPos[0], self.foodPos[1], 10, 10))