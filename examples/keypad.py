from guizero import App, Box, PushButton, TextBox

app = App(width=300, height=300)

text = TextBox(app, text="0", width="fill")

b = Box(app, layout="grid", width="fill")
button1 = PushButton(b, text="1", grid=[0,0])
button2 = PushButton(b, text="2", grid=[1,0])
button3 = PushButton(b, text="3", grid=[2,0])
buttonPlus = PushButton(b, text="+", grid=[3,0])
button4 = PushButton(b, text="4", grid=[0,1])
button5 = PushButton(b, text="5", grid=[1,1])
button6 = PushButton(b, text="6", grid=[2,1])
buttonMinus = PushButton(b, text="-", grid=[3,1])
button7 = PushButton(b, text="7", grid=[0,2])
button8 = PushButton(b, text="8", grid=[1,2])
button9 = PushButton(b, text="9", grid=[2,2])
buttonSquare = PushButton(b, text="*", grid=[3,2])
buttonComma = PushButton(b, text=",", grid=[0,3])
button0 = PushButton(b, text="0", grid=[1,3])
buttonPlusMinus = PushButton(b, text="+/-", grid=[2,3])
buttonDivided = PushButton(b, text="/", grid=[3,3])
btnUguale = PushButton(b, text="=", grid=[4,0,4,1])


app.display()
