from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Pulsante")

def cambiaTitolo():
    titolo = window.title()
    if titolo == "Pulsante":
        window.title("Titolo cambiato!!!")
        return
    window.title("Pulsante")
    return

btn = Button(window, text="Cambia Titolo", command=cambiaTitolo) 
btn.grid(column=0, row=0, padx=50, pady=20)
window.mainloop()