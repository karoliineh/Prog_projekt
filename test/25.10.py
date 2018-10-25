from tkinter import *

blankwindow = Tk() ##teeb tühja akna
## kõik window värk siin vahel
def funktsioon(a):
    print("Yo, dawg")

header = Frame(blankwindow)
header.pack()
footer = Frame(blankwindow)
footer.pack(side=BOTTOM)

nupp1 = Button(footer, text = "Vajuta mind, yes", fg="purple", bg="white")
nupp2 = Button(footer, text = "Vajuta mind ka, ooh", fg="yellow", bg="black")
nupp3 = Button(footer, text = "Vajuta mind ka, yes", fg="purple")

nupp1.pack(side=LEFT)
nupp1.bind("<Button-1>", funktsioon)
nupp2.pack(side=LEFT)
nupp3.pack(side=BOTTOM)

tekst_1 = Label(header, text="Kasutajanimi")
tekst_2 = Label(header, text="Parool")
sisestus_1 = Entry(header, bg="purple")
sisestus_2 = Entry(header, bg="white")

tekst_1.grid(row=0, sticky=E)
tekst_2.grid(row=1, sticky=E)

sisestus_1.grid(row=0, column=1)
sisestus_2.grid(row=1, column=1)

c = Checkbutton(header, text="Hoia mind sisselogituna")
c.grid(columnspan=2)



## kõik window värk siin vahel
blankwindow.mainloop()