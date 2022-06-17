from guizero import *
raiz = App("Práctica con Box")

caja = Box(raiz,align="left", width="fill", border=2)
caja1 = Box(raiz,align="top", width=200, height=300, border=3)
caja2 = Box(raiz,align="left", width=120, height=70, border=5)

texto1 = Text(caja, text="Este es un boton:")
btn_1 = PushButton(caja)

texto2 = Text(caja1, text="Es un checkbutton")
btn_2 = CheckBox(caja1)

texto2 = Text(caja2, text="Es un slider")
btn_3 = Slider(caja2)




raiz.display()