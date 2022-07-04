#!/bin/python3
from guizero import *
app_name = 'Procesador de texto simple - guizero'
app_version = '1'
app_verdate = '13-DEC-2019'
app_version_string = app_name + ' v' + app_version + ' (' + app_verdate + ')'

def push_grabar():
    with open(nombreArchivo.value, "w") as f:
        f.write(escritorio.value)
    btn_save.disable()


def push_leer():
    with open(nombreArchivo.value, "r") as f:
        escritorio.value = f.read()


def menu_abrir():
    f = raiz.select_file(title="Select file", folder=".", filetypes=[
                         ["Archivos de Texto", "*.txt"]], save=False)
    nombreArchivo.value = f
    push_leer()

def menu_guardar():
    f = raiz.select_file(title="Select file", folder=".", filetypes=[
                         ["Archivos de Texto", "*.txt"]], save=True)
    nombreArchivo.value = f
    push_grabar()


def menu_salir():
    w = yesno("Salir", "¿Quieres Salir sin grabar?")
    print(w)
    if w:
        raiz.destroy()
    else:
        pass

def make_dark_mode():
        raiz.bg = "black"
        raiz.text_color = "white"
        btn_darkmode.hide()
        btn_darkmode1.show()

def make_claro_mode():
        raiz.bg="white"
        raiz.text_color="black"
        btn_darkmode1.hide()
        btn_darkmode.show()

    
def menu_acerca_de():
    info("Acerca de", app_version_string)


def cambiar_fuente():
    escritorio.font = tipo_letra.value


def cambiar_tamano_texto():
    escritorio.text_size = tamano.value
    escritorio.resize(1, 1)
    escritorio.resize("fill", "fill")
    # resize the widget because if the text is made bigger, this might
    # affect the size of the TextBox so guizero needs to know how to maintain the intended layout


def cambiar_color():
    escritorio.text_color = text_color.value

def enable_btn_save():
    btn_save.enable()


raiz = App(title="Procesador de Textos", width=550)

caja = Box(raiz, align="top", width="fill", border=2)

nombreArchivo = TextBox(caja, text="archivo.txt", width=38, align="left")


barra_menu = MenuBar(raiz,
                     toplevel=["Archivo", "Ayuda"],
                     options=[
                         [["Abrir", menu_abrir], ["Guardar", menu_guardar],["Salir", menu_salir]],
                         [["Acerca de", menu_acerca_de]]
                    ])



btn_save = PushButton(caja, text="Grabar", align="right", command=push_grabar)
btn_read = PushButton(caja, text="  Leer  ", align="right", command=push_leer)
btn_darkmode = PushButton(caja, text="ModoOscuro", align="right", command=make_dark_mode)
btn_darkmode1 = PushButton(caja, text="ModoClaro", align="right", command=make_claro_mode, visible=False)




escritorio = TextBox(raiz, width="fill", height="fill", multiline=True, command=enable_btn_save)

barra_control = Box(raiz, align="bottom", width="fill", border=True)
tipo_letra = Combo(barra_control, options=[
                   "courier", "times new roman", "verdana"], align="left", command=cambiar_fuente)

tamano = Slider(barra_control, align="left",
                command=cambiar_tamano_texto, start=10, end=18)

text_color = Combo(barra_control, options=[
                   'black', 'blue', 'red', 'magenta', 'yellow'], align="left", selected='black', command=cambiar_color)
btn_save.disable()

raiz.display()
