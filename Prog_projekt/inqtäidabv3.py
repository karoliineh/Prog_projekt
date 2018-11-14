from tkinter import *


class jaotus:
    
    def __init__(self, master):
        mvar = IntVar()
        
        def laud_eest(self):
            canvas.delete("all") ## kustutab igal nupuvajutusel
            ## 1. punkti (X, Y) koordinaadid, 2. punkti (X, Y) koordinaadid
            ## Antud funktsioonis ei ole laius_callback'i kordagi kasutatud, sest üritasin saavutada kõigest 2D pilti.
            ## Muutujate jalg2;3;4 (ehk parempoolse jala kolm joont) juures on lahutatud mingid arvud pikkus_callbackist selleks,
            ## et kogu jalg sõltuvalt laua pikkusest ikka tasakaalu võimaldavas positsioonis oleks.
            tasapind1 = canvas.create_line(50, 50, pikkus_callback(self), 50) 
            tasapind2 = canvas.create_line(50, 75, pikkus_callback(self), 75)
            tasapind3 = canvas.create_line(50, 50, 50, 75)
            tasapind4 = canvas.create_line(pikkus_callback(self), 50, pikkus_callback(self), 75)
            jalg1 = canvas.create_line(60, 75, 60, kõrgus_callback(self))
                #jalg2 = canvas.create_line(790, 75, 790, kõrgus_callback(self))
            jalg2 = canvas.create_line(pikkus_callback(self) - 10, 75, pikkus_callback(self) - 10, kõrgus_callback(self))
            jalg3 = canvas.create_line(75, 75, 75, kõrgus_callback(self))
                #jalg4 = canvas.create_line(775, 75, 775, kõrgus_callback(self))
            jalg4 = canvas.create_line(pikkus_callback(self) - 25, 75, pikkus_callback(self) - 25, kõrgus_callback(self))
            jalg5 = canvas.create_line(60, kõrgus_callback(self), 75, kõrgus_callback(self))
                #jalg6 = canvas.create_line(775, kõrgus_callback(self), 790, kõrgus_callback(self))
            jalg6 = canvas.create_line(pikkus_callback(self) - 25, kõrgus_callback(self), pikkus_callback(self) - 10, kõrgus_callback(self)) 
            return tasapind1, tasapind2, tasapind3, tasapind4, jalg1, jalg2, jalg3, jalg4, jalg5, jalg6
        
        # dimensioon callback funktsioonid fetchivad dimensiooniväljadesse kirjutatud numbrid,
        # mida omakorda saab laud_eest funktsioonis kasutusse võtta
        
        def pikkus_callback(self):
            callback = pikkus_s.get() 
            return int(callback)
        
        def laius_callback(self):
            callback = laius_s.get()
            return int(callback)
        
        def kõrgus_callback(self):
            callback = kõrgus_s.get()
            return int(callback)
        
        header = Frame(master)
        header.pack()
        
        canvas = Canvas(master, width=3508, height=2480, bg="white")
        canvas.pack(side=BOTTOM)
        
        footer = Frame(master)
        footer.pack(side=BOTTOM)
        
        pikkus = Label(header, text="Pikkus (mm)")
        laius = Label(header, text="Laius (mm)")
        kõrgus = Label(header, text="Kõrgus (mm)")
        pikkus_s = Entry(header, bg="white")
        laius_s = Entry(header, bg="white")
        kõrgus_s = Entry(header, bg="white")
        
        tühi_tulp = Label(header, text="    ")
        tühi_tulp2 = Label(header, text= 200*" ")

        pikkus.grid(row=0, sticky=E)
        laius.grid(row=1, sticky=E)
        kõrgus.grid(row=2, sticky=E)

        pikkus_s.grid(row=0, column=1)
        laius_s.grid(row=1, column=1)
        kõrgus_s.grid(row=2, column=1)
        tühi_tulp.grid(column=2)
        tühi_tulp2.grid(column=5)
        
        tagaserv = Checkbutton(header, text="Tagaservaga", state= ACTIVE, variable = mvar)
        tagaserv.grid(row=1, column=3)
        
##        joonista = Button(header, text = "Valmis", fg="black", bg="white")
##        joonista.grid(row=1, column=4)
##        joonista.bind("<Button-1>", laud_eest)
        
        self.nupp1 = Button(header, text="See on nupp")
        self.nupp1.grid(row=1, column=4)
        self.nupp1.bind("<Button-1>", pikkus_callback)
        self.nupp1.bind("<Button-1>", laius_callback)
        self.nupp1.bind("<Button-1>", kõrgus_callback)
        self.nupp1.bind("<Button-1>", laud_eest)

root = Tk()
## kõik window värk siin vahel

objekt = jaotus(root)

## kõik window värk siin vahel
root.mainloop()