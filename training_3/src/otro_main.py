from gestor_de_prediccion import Gestor
from modelo_boton import Modelo_Boton
#import gestor_de_prediccion
#from gestor_de_prediccion import Gestor
#from gestor_de_prediccion import Gestor
from Tkinter import *

lista_botones = []


def crear_boton(nombre, top):
    boton_aux = Button(top, text=nombre, command=lambda: escribiente.escribir(nombre))
    lista_botones.append(boton_aux)
    lista_botones[len(lista_botones) -1].pack()

root = Tk()
i = 0
while i < 10:
    crear_boton(str(i), root)
    i = i + 1
crear_boton('OK',root)
text = Text(root)
text.pack()
text.insert(INSERT, 'agregando palabra: \n')


diccionario_de_botones = {\
              '0': '',
              '1': '',
              '2': ['a', 'b', 'c'],
              '3': ['d', 'e', 'f'],
              '4': ['g', 'h', 'i'],
              '5': ['j', 'k', 'l'],
              '6': ['m', 'n', 'o'],
              '7': ['p', 'q', 'r', 's'],
              '8': ['t', 'u', 'v'],
              '9': ['w', 'x', 'y', 'z'],
               '#': ' ', '*': ''
              }


class Escribiente():
    def disminuir_indice(self):
        lista = text.index(INSERT).split('2.')
        indice_num = int(lista[1]) - 1
        indice_str = '2.' + str(indice_num)
        return indice_str

    def escribir(self, boton):
        if boton != 'OK':
            if boton == self.anterior_boton:
                text.delete(self.disminuir_indice(), END)
                self.seleccion_letra = self.seleccion_letra + 1
            else:
                self.seleccion_letra = 0
            try:
                text.insert(INSERT, self.traer_caracter(boton))
            except:
                self.seleccion_letra = 0
                text.insert(INSERT, self.traer_caracter(boton))
            self.anterior_boton = boton
        else:
            print text.get('2.1', INSERT)

    def traer_caracter(self, boton):
        for tupla in diccionario_de_botones.items():
            if tupla[0] == boton:
                return tupla[1][self.seleccion_letra]

    def __init__(self):
        self.palabra = ''
        self.incompleta = True
        self.seleccion_letra = 0
        self.anterior_boton = ''

escribiente = Escribiente()





def main():
    text.insert(INSERT, ' ')
    root.mainloop()

if __name__ == '__main__':
    main()

