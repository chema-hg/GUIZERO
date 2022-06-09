#gui de ventanas usando la libreria guizero 
#instalarla con sudo pip3 install guizero

from guizero import App, Text

raiz = App(title="Esta es mi primera GUI")

primer_mensaje = Text(raiz, text="This is big text!.")
primer_mensaje.text_size = 40


segundo_mensaje = Text(raiz, "this is green")
segundo_mensaje.bg = "green"  # bg = back ground colour

tercer_mensaje = Text(raiz, text="today is monday")
tercer_mensaje.text_color = "red"
tercer_mensaje.font = "times new roman"
# tambien se puede poner tercer_mensaje = Text(raiz, "hoy es lunes", color="red", size=40, font="helvetica")

raiz.display()  # muestra en pantalla y hace un loop infinito
