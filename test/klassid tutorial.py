from tkinter import *


class seeonuseful:
    
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        
        self.nupp1 = Button(frame, text="See on nupp", command=self.funktsioon)
        self.nupp1.pack(side=LEFT)
        
        self.nupp2 = Button(frame, text="Välju", command=frame.quit) ##sama funktsioon, mis X, aga miskiprst ei toimi
        self.nupp2.pack(side=LEFT)
        
        
    def funktsioon(self):
        print("Yayyyyyy")


root = Tk()
objekt = seeonuseful(root)
root.mainloop()