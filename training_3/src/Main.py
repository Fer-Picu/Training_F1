'''
Created on 26/03/2013

@author: fernando
'''
from Tkinter import *
from gestor_de_prediccion import Gestor


mi_gestor = Gestor()
texto_1 = Text()
texto_1.config(width=60, height=15)
texto_1.pack()
texto_2 = Text()
texto_2.pack()


class Gestor_De_Escritura():

    diccionario_letras = {\
                          '0': '',
                          '1': '',
                          '2': ['a', 'b', 'c'],
                          '3': ['d', 'e', 'f'],
                          '4': ['g', 'h', 'i'],
                          '5': ['j', 'k', 'l'],
                          '6': ['m', 'n', 'o'],
                          '7': ['p',  'q', 'r', 's'],
                          '8': ['t', 'u', 'v'],
                          '9': ['w', 'x', 'y', 'z'],
                           '#': ' ', '*': ''
                          }

    def start_to_write_new_word(self, tecla):
        self.indice_nueva_palabra = texto_1.insert
        texto_1.insert(INSERT, self.diccionario_letras[tecla][0])

    def cambiar_opcion(self):
        texto_1.delete(self.principio_palabra, self.fin_palabra)
        self.principio_palabra = texto_1.index(CURRENT)
        try:
            texto_1.insert(INSERT, self.mis_opciones[self.seleccion])
        except:
            pass
        self.fin_palabra = texto_1.index(CURRENT)

    def espacio(self):
        print texto_1.index(CURRENT), ' ', texto_1.index(INSERT), '',\
                                texto_1.index(END)
        texto_1.insert(END, ' ')
        print 'a'
        self.linea = ''
        texto_2.delete(1.0, END)
        self.mis_opciones = []

    def continue_write_word(self, word):
        self.mis_opciones = mi_gestor.buscar_opciones(word)
        if self.mis_opciones != []:
            texto_2.delete(1.0, END)
            for opcion in self.mis_opciones:
                texto_2.insert(INSERT, opcion)
                texto_2.insert(INSERT, '\n')
            texto_1.delete(self.principio_palabra, INSERT)
            texto_1.insert(INSERT, word)
        else:
            print 'agregar palabra???'

    def __init__(self):
        self.linea = ''
        self.seleccion = 0
        self.mis_opciones = []
        self.palabra_completa = True
        self.indice_nueva_palabra = ""

    def analis_text(self, clave_boton):
        self.palabra_completa = False
        if self.linea == '':
            print texto_1.index(CURRENT), ' ', texto_1.index(INSERT), '',\
                                texto_1.index(END)
            self.principio_palabra = texto_1.index(INSERT)
            self.start_to_write_new_word(clave_boton)
            self.linea = self.diccionario_letras[clave_boton][0]
        else:
            self.letra = self.diccionario_letras[clave_boton][0]
            self.linea = self.linea + self.letra
            self.continue_write_word(self.linea)
            self.fin_palabra = texto_1.index(INSERT)
            print texto_1.index(CURRENT), ' ', texto_1.index(INSERT), ' ',\
                                texto_1.index(END)

gestor_de_escritura = Gestor_De_Escritura()


class Interprete_Boton():
    def interpretar(self, boton):
        try:
            boton = int(boton)
            gestor_de_escritura.analis_text(str(boton))
        except:
            self.comando(boton)

    def comando(self, comando):
        if comando == 'clear':
            print gestor_de_escritura.linea
            try:
                print 'la ultima letra es : ', \
                    gestor_de_escritura.linea[\
                                        len(gestor_de_escritura.linea) - 1]
            except:
                pass
        if comando == "ok":
            texto_1.delete(gestor_de_escritura.principio_palabra, gestor_de_escritura.fin_palabra)
            pass
        if comando == '#':
            gestor_de_escritura.espacio()
        if comando == "right":
            pass
        if comando == "left":
            pass
        if comando == "down":
            gestor_de_escritura.seleccion = gestor_de_escritura.seleccion\
                                             + 1
            try:
                gestor_de_escritura.cambiar_opcion()
            except:
                gestor_de_escritura.seleccion = 0
                gestor_de_escritura.cambiar_opcion()
        if comando == "up":
            gestor_de_escritura.seleccion = gestor_de_escritura.seleccion\
                                         - 1
            try:
                gestor_de_escritura.cambiar_opcion()
            except:
                gestor_de_escritura.seleccion = 0
                gestor_de_escritura.cambiar_opcion()

    def __init__(self):
        pass
control = Interprete_Boton()
lista_botones = []


def crear_boton(nombre, top):
    boton_aux = Button(top, text=nombre,\
                    command=lambda: control.interpretar(nombre))
    lista_botones.append(boton_aux)
    lista_botones[len(lista_botones) - 1].pack()
if __name__ == '__main__':
    top = Tk()
    print 'hasta'
    i = 1
    while i < 10:
        crear_boton(str(i), top)
        i = i + 1
    crear_boton('clear', top)
    crear_boton('up', top)
    crear_boton('down', top)
    crear_boton('left', top)
    crear_boton('right', top)
    crear_boton('ok', top)
    crear_boton('#', top)
    top.mainloop()

