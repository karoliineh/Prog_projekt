from tkinter import *

def midagi():
    print("see on midagi")
    
root = Tk()

menüü = Menu(root)
root.config(menu=menüü)

subMenüü = Menu(menüü, tearoff=0)  ## tearoff - Remove the dashed line (- - - - - - - -) above the dropdown list
menüü.add_cascade(label="file", menu=subMenüü)
subMenüü.add_command(label="uus projekt", command=midagi)
subMenüü.add_command(label="uus ..", command=midagi)
subMenüü.add_separator()
subMenüü.add_command(label="Välju", command=midagi)

editMenu = Menu(menüü)
menüü.add_cascade(label="Teine drop", menu=editMenu)
editMenu.add_command(label="uus..", command=midagi)

root.mainloop()