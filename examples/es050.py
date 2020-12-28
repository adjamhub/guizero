from guizero import App, Slider, Text

def slider_changed(slider_value):
    testo.value = "il valore attuale dello slider è " + slider_value

app = App()
slider = Slider(app, command=slider_changed)
testo = Text(app)

app.display()
