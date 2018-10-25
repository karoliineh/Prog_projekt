from tkinter import *

root = Tk()

canvas = Canvas(root, width=400, height=300)
canvas.pack()

mustjoon = canvas.create_line(20, 50, 100, 100)
lillajoon = canvas.create_line(100, 100, 100, 200, fill="purple")

root.mainloop()