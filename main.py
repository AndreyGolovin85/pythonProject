from tkinter import *
import setting as sg
from math import *
f = input('f(x): ')
root = Tk()
root.title("Графики")
# Настраиваем окно
canvas = Canvas(root, width=sg.width_screen, height=sg.height_screen, bg="lightblue",
                cursor="pencil")
# Рисуем оси координат
canvas.create_line(400, 800, 400, 0, width=2, arrow=LAST)
canvas.create_line(0, 400, 800, 400, width=2, arrow=LAST)

first_x = -500
for i in range(16000):
    if(i % 800 == 0):
        k = first_x + (1/16) * i
        k = int(k)
        # Рисуем координаты оси x.
        canvas.create_line(k + 400, -3 + 400, k + 400, 3 + 400, width=0.5,
                           fill='black')
        canvas.create_text(k + 400, 390, text=str(k), fill='purple',
                           font=('Helvectica', '7'))
        # Рисуем координаты оси y.
        canvas.create_line(-3 + 400, k + 400, 3 + 400, k + 400, width=0.5,
                           fill='black')
        canvas.create_text(415, -k + 400, text=str(k), fill='purple',
                           font=('Helvectica', '7'))
        try:
            x = first_x + (1/16) * i
            new_f = f.replace('x', str(x))
            y = -eval(new_f)+400
            x += 400
            canvas.create_oval(x, y, x + 1, y + 1, width=5, fill='black')
        except:
            pass
canvas.pack()
root.mainloop()
