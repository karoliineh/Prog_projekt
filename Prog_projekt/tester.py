from tkinter import *

def callback():
    print(pikkus_s.get())

root = Tk()
## kõik window värk siin vahel

header = Frame(root)
header.pack()

pikkus = Label(header, text="Pikkus (mm)")
laius = Label(header, text="Laius (mm)")
kõrgus = Label(header, text="Kõrgus (mm)")
pikkus_s = Entry(header, bg="white")
laius_s = Entry(header, bg="white")
kõrgus_s = Entry(header, bg="white")

b = Button(header, text="get", width=10, command=callback)
b.grid(row=0, column=2)

pikkus_sisend = pikkus_s.get()
laius_sisend = laius_s.get()
kõrgus_sisend = kõrgus_s.get()


pikkus.grid(row=0, sticky=E)
laius.grid(row=1, sticky=E)
kõrgus.grid(row=2, sticky=E)

pikkus_s.grid(row=0, column=1)
laius_s.grid(row=1, column=1)
kõrgus_s.grid(row=2, column=1)





## kõik window värk siin vahel
root.mainloop()