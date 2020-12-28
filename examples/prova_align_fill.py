from guizero import App, Text, TextBox, PushButton
app = App(height=100)
text = Text(app, text="label", align="left")
text_box = TextBox(app, text="enter text", align="left",width="fill")
button = PushButton(app, text="submit", align="left")
app.display()