'''
Created on 26/03/2013

@author: fernando
'''
from Tkinter import *

top = Tk()
texto_1 = Text()
texto_1.pack()
marca_actual = texto_1.mark_set('principio', CURRENT)
lista_2 = ['a', 'b', 'c']


class Gestor_De_Eescritura():
    linea = ''
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
    lista_de_palabras = [\
                         'hola', 'bien', 'horario', 'termo',
                         'temple', 'accion', 'cancion', 'estar',
                         'escribo', 'aviso', 'que', 'veces', 'burundanga'
                        ]

    def start_to_write_new_word(self, tecla):
        texto_1.insert(INSERT, self.diccionario_letras[tecla][0])
        pass

    def __init__(self):
        pass

    def analis_text(self, boton):
        if self.linea == '':
            self.start_to_write_new_word(boton)
            self.linea = self.diccionario_letras[boton][2]
        else:
            self.letra = self.diccionario_letras[boton][1]
#             print type(self.letra)
            self.linea = self.linea + self.letra
            print self.linea

gestor = Gestor_De_Eescritura()

if __name__ == '__main__':
    boton_hola = Button(top, text="Hello",\
                         command=lambda: gestor.analis_text("Hello"))
    boton_hola.pack()
    boton_1 = Button(top, text='1',
                     command=lambda: gestor.analis_text("1"))
    boton_1.pack()
    boton_2 = Button(top, text='2',
                     command=lambda: gestor.analis_text("2"))
    boton_2.pack()
    boton_3 = Button(top, text='3',
                     command=lambda: gestor.analis_text("3"))
    boton_3.pack()
    boton_4 = Button(top, text='4',
                     command=lambda: gestor.analis_text("4"))
    boton_4.pack()
    boton_5 = Button(top, text='5',
                     command=lambda: gestor.analis_text("5"))
    boton_5.pack()
    boton_6 = Button(top, text='6',
                     command=lambda: gestor.analis_text("6"))
    boton_6.pack()
    boton_7 = Button(top, text='7',
                     command=lambda: gestor.analis_text("7"))
    boton_7.pack()
    boton_8 = Button(top, text='8',
                     command=lambda: gestor.analis_text("8"))
    boton_8.pack()
    boton_9 = Button(top, text='9',
                     command=lambda: gestor.analis_text("9"))
    boton_9.pack()
    boton_clear = Button(top, text='clear',
                     command=lambda: gestor.analis_text("9"))
    boton_clear.pack()
    boton_ok = Button(top, text='ok',
                     command=lambda: gestor.analis_text("9"))
    boton_ok.pack()
    boton_left = Button(top, text='left',
                     command=lambda: gestor.analis_text("9"))
    boton_left.pack()
    boton_right = Button(top, text='right',
                     command=lambda: gestor.analis_text("9"))
    boton_right.pack()
    boton_up = Button(top, text='up',
                     command=lambda: gestor.analis_text("9"))
    boton_up.pack()
    boton_down = Button(top, text='down',
                     command=lambda: gestor.analis_text("9"))
    boton_down.pack()
    top.mainloop()
