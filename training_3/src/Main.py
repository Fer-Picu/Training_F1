'''
Created on 26/03/2013

@author: fernando
'''
from Tkinter import *
from gestor_de_prediccion import Gestor


top = Tk()
texto_1 = Text()
texto_1.pack()
marca_actual = texto_1.mark_set('principio', CURRENT)
lista_2 = ['a', 'b', 'c']
mi_gestor = Gestor()


class Gestor_De_Eescritura():

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
        texto_1.insert(INSERT, self.diccionario_letras[tecla][0])

    def continue_write_word(self, word):
        print mi_gestor.buscar_opciones(word)

    def __init__(self):
        self.linea = ''

    def analis_text(self, clave_boton):
        if self.linea == '':
            self.start_to_write_new_word(clave_boton)
            self.linea = self.diccionario_letras[clave_boton][0]
        else:
            self.letra = self.diccionario_letras[clave_boton][0]
            self.linea = self.linea + self.letra
            self.continue_write_word(self.linea)

gestor_de_escritura = Gestor_De_Eescritura()


class Interprete_Boton():
    def interpretar(self, boton):
        if boton == 'clear' or 'ok' or 'right' or 'up' or'down' or 'left':
            self.comando(boton)
        else:
            gestor_de_escritura.analis_text(boton)

    def comando(self, comando):
        if comando == "clear":
            print 'clear'
            print gestor_de_escritura.linea
            try:
                print gestor_de_escritura.linea[len(gestor_de_escritura.linea)\
                                                - 1]
            except:
                pass
        if comando == "ok":
            pass
        if comando == "right":
            pass
        if comando == "left":
            pass
        if comando == "up":
            pass
        if comando == "down":
            pass

    def __init__(self):
        pass
control = Interprete_Boton()
if __name__ == '__main__':
    print 'hasta'
    boton_hola = Button(top, text="Hello",\
                    command=lambda: control.comando("Hello"))
    boton_hola.pack()
    boton_1 = Button(top, text='1',
                     command=lambda: control.comando("1"))
    boton_1.pack()
    boton_2 = Button(top, text='2',
                     command=lambda: control.comando("2"))
    boton_2.pack()
    boton_3 = Button(top, text='3',
                     command=lambda: control.comando("3"))
    boton_3.pack()
    boton_4 = Button(top, text='4',
                     command=lambda: control.comando("4"))
    boton_4.pack()
    boton_5 = Button(top, text='5',
                     command=lambda: control.comando("5"))
    boton_5.pack()
    boton_6 = Button(top, text='6',
                     command=lambda: control.comando("6"))
    boton_6.pack()
    boton_7 = Button(top, text='7',
                     command=lambda: control.comando("7"))
    boton_7.pack()
    boton_8 = Button(top, text='8',
                     command=lambda: control.comando("8"))
    boton_8.pack()
    boton_9 = Button(top, text='9',
                     command=lambda: control.comando("9"))
    boton_9.pack()
    boton_clear = Button(top, text='clear',
                     command=lambda: control.comando("clear"))
    boton_clear.pack()
    boton_ok = Button(top, text='ok',
                     command=lambda: control.comando("ok"))
    boton_ok.pack()
    boton_left = Button(top, text='left',
                     command=lambda: control.comando("left"))
    boton_left.pack()
    boton_right = Button(top, text='right',
                     command=lambda: control.comando("right"))
    boton_right.pack()
    boton_up = Button(top, text='up',
                     command=lambda: control.comando("up"))
    boton_up.pack()
    boton_down = Button(top, text='down',
                     command=lambda: control.comando("down"))
    boton_down.pack()
    top.mainloop()
    print 'aca'
