## NOTES TO SELF (Karo)
## Mõõdud ei meigi vasjee sensi
## Oleks tore, kui mõõdud ka nt. joonise peale saaks
## ISO vaade ka, siis juba suht esituskõlblik, hehe :P

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
            tasapind2 = canvas.create_line(50, 61, pikkus_callback(self), 61)
            tasapind3 = canvas.create_line(50, 50, 50, 61)
            tasapind4 = canvas.create_line(pikkus_callback(self), 50, pikkus_callback(self), 61)
            jalg1 = canvas.create_line(60, 61, 60, kõrgus_callback(self) -11)
                #jalg2 = canvas.create_line(790, 75, 790, kõrgus_callback(self))
            jalg2 = canvas.create_line(pikkus_callback(self) - 10, 61, pikkus_callback(self) - 10, kõrgus_callback(self) -11)
            jalg3 = canvas.create_line(70, 61, 70, kõrgus_callback(self) -11)
                #jalg4 = canvas.create_line(775, 75, 775, kõrgus_callback(self))
            jalg4 = canvas.create_line(pikkus_callback(self) - 20, 61, pikkus_callback(self) - 20, kõrgus_callback(self) -11)
            jalg5 = canvas.create_line(60, kõrgus_callback(self) -11, 70, kõrgus_callback(self) -11)
                #jalg6 = canvas.create_line(775, kõrgus_callback(self), 790, kõrgus_callback(self))
            jalg6 = canvas.create_line(pikkus_callback(self) - 20, kõrgus_callback(self) -11, pikkus_callback(self) - 10, kõrgus_callback(self) -11) 
    
        
         ## ----- 14.11 Karoliine ------
         ## ----- laud küljelt ---------
        
            tasapind5 = canvas.create_line(700, 50, 700+laius_callback(self), 50) 
            tasapind6 = canvas.create_line(700, 61, 700+laius_callback(self), 61)
            tasapind7 = canvas.create_line(700, 50, 700, 61)
            tasapind8 = canvas.create_line(700+laius_callback(self), 50, 700+laius_callback(self), 61)
            jalg7 = canvas.create_line(720, 61, 720, kõrgus_callback(self) -11)
                #jalg2 = canvas.create_line(790, 75, 790, kõrgus_callback(self))
            jalg8 = canvas.create_line(700+laius_callback(self) - 10, 61, 700+laius_callback(self) - 10, kõrgus_callback(self) -11)
            jalg9 = canvas.create_line(730, 61, 730, kõrgus_callback(self) -11)
                #jalg4 = canvas.create_line(775, 75, 775, kõrgus_callback(self))
            jalg10 = canvas.create_line(700+laius_callback(self) - 20, 61, 700+laius_callback(self) - 20, kõrgus_callback(self) -11)
            jalg11 = canvas.create_line(720, kõrgus_callback(self) -11, 730, kõrgus_callback(self) -11)
                #jalg6 = canvas.create_line(775, kõrgus_callback(self), 790, kõrgus_callback(self))
            jalg12 = canvas.create_line(700+laius_callback(self) - 20, kõrgus_callback(self) -11, 700+laius_callback(self) - 10, kõrgus_callback(self) -11) 
            return tasapind1, tasapind2, tasapind3, tasapind4, jalg1, jalg2, jalg3, jalg4, jalg5, jalg6, tasapind5, tasapind6, tasapind7, tasapind8, jalg7, jalg8, jalg9, jalg10, jalg11, jalg12
        
        ## ----- 14.11 Karoliine ------
        
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
        
        pikkus = Label(header, text="Pikkus (cm)")
        laius = Label(header, text="Laius (cm)")
        kõrgus = Label(header, text="Kõrgus (cm)")
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
        
##      ---- peitsin selle nupu ära, hihi------
##        tagaserv = Checkbutton(header, text="Tagaservaga", state= ACTIVE, variable = mvar)
##        tagaserv.grid(row=1, column=3)

        
        self.nupp1 = Button(header, text="Joonista", fg="black", bg="white")
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