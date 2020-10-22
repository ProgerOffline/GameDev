import random
import time

# Логика приложения
class Generator:
	def __init__(self):
		"""Создание основных преременных"""

		self.begin = 0
		self.end = 0
		self.numInList = 0
		self.comb = 0

		self.whiteList = []
		self.numbers = [] 
		self.cashNumbers = [] 
		self.outList = []

	def mainMethod(self, n1, n2, n3, n4):
		# создать список от begin 
		self.begin = int(n1)
		# До end+1
		self.end = int(n2)
		# пары из чисел от 1 до numInList
		self.numInList = int(n3)
		# кол-во комбинаций  
		self.comb = int(n4) 
		# создаем список в диапазоне от 1 до n+1 
		self.numbers = [i for i in range(self.begin, self.end + 1)]

		self.createOutList()

	"""Этот метод вызывается вместе с createOutList()"""
	def createWhiteList(self):
		"""Создаем список с числами outList"""
		"""Числа уже не повторяються"""

		# Перебор комбинаций в outList
		for num in self.outList:
			# Если комбинации нет в списке
			if not num in self.whiteList:
				self.whiteList.append(" ".join(num))

		self.createOutTxt()

	"""Этот метод вызывается вместе с mainMethod()"""
	def createOutList(self):
		"""Создаем список из чисел типа [43, 23, 22, 11] и т.д."""
		"""Которые могу повторяться"""

		# Повторять пока не заполниться outList
		while len(self.outList) == 0 or len(self.outList) < self.comb:
			# Выбираем из диапазона чисел случайное и добавляем
			choice = str(random.choice(self.numbers))

			# Если элемент есть добавляем
			# Если элемента нет, не добавляем
			if choice in self.cashNumbers:
				pass
			else:
				self.cashNumbers.append(choice)

			self.checkFill()

		self.createWhiteList()

	"""Этот метод вызывается вместе с createOutList()"""
	def checkFill(self):
		"""Проверяем заполнение списка, чтобы кол-во"""
		"""Цифр в списке было равно заданному значению numInList"""

		if len(self.cashNumbers) == self.numInList:
			self.outList.append(self.cashNumbers)
			self.cashNumbers = []
		
	"""Этот метод вызывается вместе с createWhiteList()"""
	def createOutTxt(self):
		"""Создаем файл со списком whiteList/комбинациями"""

		file = open("out.txt", "w")
		file.write("\n".join(self.whiteList))

		self.begin = 0
		self.end = 0
		self.numInList = 0 
		self.comb = 0

		self.whiteList = []  
		self.numbers = [] 
		self.cashNumbers = [] 
		self.outList = []