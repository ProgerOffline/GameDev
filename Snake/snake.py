import pygame
from colors import *

class Snake:
	def __init__(self):

		self.head = [45, 45]
		self.body = [[45, 45], [34, 45]]
		self.speed = 11

	def move(self, keyMove):
		"""Движение змеи в зависимости от направлениея (Control.flagDirection)"""
		if keyMove.flagDirection == "RIGHT":
			self.head[0] += self.speed
		elif keyMove.flagDirection == "LEFT":
			self.head[0] -= self.speed
		elif keyMove.flagDirection == "UP":
			self.head[1] -= self.speed
		elif keyMove.flagDirection == "DOWN":
			self.head[1] += self.speed

	def animation(self):
		"""Прибавляем в начало списка тела голову, а хвост удаляем"""
		self.body.insert(0, list(self.head))
		self.body.pop()

	def drawSnake(self, screen):
		"""Отрисовка змеи на поле"""
		for segment in self.body:
			pygame.draw.rect(screen, purple, pygame.Rect(segment[0], segment[1], 10, 10))

	def checkEndWindow(self):
		"""Проверка касания змеи краёв поля/левела/уровня"""
		if   self.head[0] == 419:   self.head[0] = 23
		elif self.head[0] == 12:    self.head[0] = 419
		elif self.head[1] == 23:    self.head[1] = 419
		elif self.head[1] == 419:   self.head[1] = 34

	def eat(self, food, gui):
		"""Реализация поедания еды"""

		if self.head == food.foodPos:
			self.body.append([food.foodPos])
			food.getFoodPos(gui)
			gui.getNewIndicator()

	def checkBarrier(self, gui):
		"""Проверяет столкновение змеи об барьер"""
		if self.head in gui.barrier:
			self.body.pop()
			gui.indicator.pop()
		if self.head in self.body[1:]:
			self.body.pop()
			gui.indicator.pop()