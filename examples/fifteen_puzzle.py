from guizero import App, PushButton

app = App(title="Fifteen Puzzle", layout="grid")
buttons = {}
i = 1
for colonna in range(4):
    for riga in range(4):
        b = PushButton(app, text=str(i),grid=[riga,colonna])
        i+=1
        indice = (riga,colonna)
        buttons[indice] = b

print(buttons)
app.display()

