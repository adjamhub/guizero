from guizero import App, Text, CheckBox, ButtonGroup, Box

a = App(title="Layout 00")
# ----------------------------
b1 = Box(a, layout="grid")
b1.bg = "yellow"
testo1 = Text(b1, text="Vista", grid=[0,0], align="top")
bgview = ButtonGroup(b1,
                     options=["Usa proprietà comuni", "Proprietà diverse per ogni cartella"],
                     grid=[1,0])
# ----------------------------
b2 = Box(a, layout="grid")
b2.bg = "lightgreen"
testo2 = Text(b2, text="Ordinamento", grid=[0,0], align="top")
sortview = ButtonGroup(b2,
                       options=["Naturale", "Alfabetico", "Alfabetico, case unsensitive"],
                       grid=[1,0])
# ----------------------------
b3 = Box(a, layout="grid")
b3.bg = "pink"
testo3 = Text(b3, text="Varie", grid=[0,0], align="top")
chk1 = CheckBox(b3, text="marcatore di selezione", grid=[1,0],align="left")
chk2 = CheckBox(b3, text="rinomina in linea", grid=[1,1],align="left")
chk3 = CheckBox(b3, text="scorri i pannelli", grid=[1,2],align="left")
chk4 = CheckBox(b3, text="chiudi la vista", grid=[1,3],align="left")

# ----------------------------
a.display()
