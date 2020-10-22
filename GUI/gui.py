from tkinter import *
from main import *

def osint():
	n1 = entry_1.get()
	n2 = entry_2.get()
	n3 = entry_3.get()
	n4 = entry_4.get()

	Generator().mainMethod(n1, n2, n3, n4)

"""Вызов класса отвечающего за логику"""

"""Обьявление основных переменных"""
WIDTH = 435
HEIGHT = 200
WINDOW_TITLE = "Генератор комбинаций"
WINDOW_ICON_PATH = "icon.ico"
  
"""Создание главного окна"""
window = Tk()
window.iconbitmap(WINDOW_ICON_PATH)
window.title(WINDOW_TITLE) 
window.geometry(str(WIDTH) + "x" + str(HEIGHT))
window.minsize(WIDTH, HEIGHT)
window.maxsize(WIDTH, HEIGHT)

"""Создание виджетов"""
empty = Label(window, text="")

entry_1 = Entry(window, justify="center")
entry_1.insert(0, "0")

entry_2 = Entry(window, justify="center")
entry_2.insert(0, "0")

label_1 = Label(window, text="Число 1")
label_2 = Label(window, text="Число 2")

entry_3 = Entry(window, justify="center")
entry_3.insert(0, "0")

entry_4 = Entry(window, justify="center")
entry_4.insert(0, "0")

label_3 = Label(window, text="Кол-во чисел в комбинации")
label_4 = Label(window, text="Кол-во комбинаций")

label_5 = Label(window, text="")

button_1 = Button(window, text="Сгенерировать", command=osint)

"""Расположение виджетов в окне"""
empty.grid(column=1, row=1)
entry_1.grid(column=1, row=2)
entry_2.grid(column=3, row=2)
label_1.grid(column=1, row=3)
label_2.grid(column=3, row=3)
entry_3.grid(column=1, row=4)
entry_4.grid(column=3, row=4)
label_3.grid(column=1, row=5)
label_4.grid(column=3, row=5)
label_5.grid(column=1, row=6)
button_1.grid(column=2, row=7)

"""Запуск главного цикла"""
window.mainloop()