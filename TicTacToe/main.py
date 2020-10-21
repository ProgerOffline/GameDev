import pygame

def check_win(mas, sign):
	zeroes = 0
	for row in mas:
		zeroes += row.count(0)
		if row.count(sign) == 3:
			return sign
	for col in range(3):
		if  mas[0][col] == sign and\
			mas[1][col] == sign and\
			mas[2][col] == sign:
			return sign
	if  mas[0][0] == sign and\
		mas[1][1] == sign and\
		mas[2][2] == sign:
		return sign
	if  mas[0][2] == sign and\
		mas[1][1] == sign and\
		mas[2][0] == sign:
		return sign
	if zeroes == 0:
		return "Ничья"
	return False

pygame.init()
sizeBlock = 100
margin = 7
width = height = sizeBlock*3 + margin*2

sizeWindow = (width, height)
screen = pygame.display.set_mode(sizeWindow)
pygame.display.set_caption("Крестики-нолики")

yellow = (255, 204, 0)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
mas = [[0]*3 for i in range(3)]

query = 0 # 1 2 3 4 5 6 7

cross = pygame.image.load("images/cross.png")
zero = pygame.image.load("images/zero.png")

game_over = False

runGame = True
while runGame:
	screen.fill(black)

	for event in pygame.event.get():
		if event.type == pygame.QUIT: runGame = False
		elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
			if event.button == 1:
				x_mouse, y_mouse = pygame.mouse.get_pos()
				col =  x_mouse // (sizeBlock + margin)
				row = y_mouse // (sizeBlock + margin)
				if mas[row][col] == 0:
					if query % 2 == 0:
						mas[row][col] = "x"

						# Выводимый текст не соответствует ходу
						# Так как во время печати уже настает ход ноликов и т.д.
						pygame.display.set_caption("Нолики ваш ход!")
					else:
						mas[row][col] = "o"

						# Выводимый текст не соответствует ходу
						# Так как во время печати уже настает ход крестиков и т.д.
						pygame.display.set_caption("Крестики ваш ход!")

					query += 1
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
			game_over = False
			mas = [[0]*3 for i in range(3)]
			query = 0
			screen.fill(yellow)

	for row in range(3):
		for col in range(3):

			x = col * sizeBlock + (col + 1) * margin
			y = row * sizeBlock + (row + 1) * margin
			pygame.draw.rect(screen, yellow, (x-3, y-3, sizeBlock-7, sizeBlock-7))

			if mas[row][col] == "x":
				screen.blit(cross, [x, y])
			elif mas[row][col] == "o":
				screen.blit(zero, [x, y])

	if (query-1) % 2 == 0: # X
		game_over = check_win(mas, "x")
	else:
		game_over = check_win(mas, "o")

	if game_over:
		screen.fill(yellow)
		pygame.display.set_caption("Крестики-нолики")

		font1 = pygame.font.SysFont('bold', 140)
		font2 = pygame.font.SysFont('sans', 16)

		text1 = font1.render(game_over, True, black)
		text2 = font2.render("Нажмите пробел чтобы начать заново.", True, black)
		text_rect = text1.get_rect()
		text_x = screen.get_width() / 2 - text_rect.width / 2
		text_y = screen.get_height() / 2 - text_rect.height / 2

		screen.blit(text1, [int(text_x), int(text_y)])
		screen.blit(text2, [screen.get_width() - (screen.get_width() - 10), 10])

	pygame.display.update()

pygame.quit()