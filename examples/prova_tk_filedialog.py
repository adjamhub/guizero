from tkinter import *
from tkinter.ttk import *

from tkinter import filedialog

# hide main window
root = Tk()
root.withdraw()

# filedialog examples
print("ESEMPIO CON askdirectory()")
percorso = filedialog.askdirectory()
print("Percorso directory:", percorso)

print("ESEMPIO CON askdopenfile()")
questo = filedialog.askopenfile()
print("fileobject:", questo)

print("ESEMPIO CON askopenfilename()")
percorso = filedialog.askopenfilename()
print("Percorso file:", percorso)

print("ESEMPIO CON askpenfilenames()")
listaPercorsi = filedialog.askopenfilenames()
print("Lista percorsi files:", listaPercorsi)

print("ESEMPIO CON askpenfiles()")
questi = filedialog.askopenfiles()
print("fileobject(s):", questi)

print("ESEMPIO CON asksaveasfile()")
quello = filedialog.asksaveasfile()
print("fileobject(s):", quello)

print("ESEMPIO CON asksaveasfilename()")
quelli = filedialog.asksaveasfilename()
print("fileobject(s):", quelli)