'''
Created on 26/03/2013

@author: fernando
'''
from Tkinter import *
from gestor_de_prediccion import Gestor


mi_gestor = Gestor()
texto_1 = Text()
texto_1.config(width=15, height=6)
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
        print 'antes'
        print self.principio_palabra, ' fin: ', self.fin_palabra
        texto_1.delete(self.principio_palabra, self.fin_palabra)
        self.principio_palabra = texto_1.index(CURRENT)
        try:
            texto_1.insert(INSERT, self.mis_opciones[self.seleccion])
        except:
            print "error cambiar opcion"
        self.fin_palabra = texto_1.index(INSERT)
        print 'despues'
        print self.principio_palabra, ' fin: ', self.fin_palabra

    def espacio(self):
        texto_1.insert(INSERT, ' ')
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
            self.sin_opciones = True
            texto_2.delete(1.0, END)
            texto_2.insert(INSERT, 'agregar palabra??? =>=> (OK) ')

    def __init__(self):
        self.linea = ''
        self.seleccion = 0
        self.mis_opciones = []
        self.indice_nueva_palabra = ""
        self.sin_opciones = False
        self.nueva_palabra_incompleta = False
        self.anterior_boton = ''
        self.palabra_a_agregar = ''

    def agregar_palabra(self):
        self.nueva_palabra_incompleta = True
        texto_2.delete(1.0, END)
        texto_2.insert(INSERT, 'AGREGANDO PALABRA: \n ')

    def terminar_de_agregar_palabra(self):
        self.palabra_a_agregar = texto_2.get('2.1', INSERT)
        self.palabra_a_agregar = str(self.palabra_a_agregar)
        mi_gestor.agregar_palabra(self.palabra_a_agregar)
        texto_1.delete(self.principio_palabra, INSERT)
        texto_1.insert(INSERT, self.palabra_a_agregar)
        texto_1.insert(INSERT, ' ')
        texto_2.delete(1.0, END)
        self.linea = ''
        self.nueva_palabra_incompleta = False

    def disminuir_indice(self):
        lista = texto_2.index(INSERT).split('2.')
        indice_num = int(lista[1]) - 1
        indice_str = '2.' + str(indice_num)
        return indice_str

    def escribir_palabra_nueva(self, boton):
        if boton == self.anterior_boton:
            texto_2.delete(self.disminuir_indice(), END)
            self.seleccion_letra = self.seleccion_letra + 1
        else:
            self.seleccion_letra = 0
        try:
            texto_2.insert(INSERT, self.traer_caracter(boton))
        except:
            self.seleccion_letra = 0
            texto_2.insert(INSERT, self.traer_caracter(boton))
        self.anterior_boton = boton

    def borrar(self, text):
        if text == texto_1:
            indice_texto = text.index(INSERT)
            lista = indice_texto.split('.')
            lista[1] = str(int(lista[1]) - 1)
            indice_texto = lista[0] + '.' + lista[1]
            text.delete(indice_texto, INSERT)
            string = str(text.get('1.0', END))
            if string.endswith(' '):
                self.linea = ''
            else:
                n = string.rfind(' ') + 1
                ahora = str(text.index(INSERT))
                lista_ahora = ahora.split('.')
                nuevo_comienzo = lista_ahora[0] + '.' + str(n)
                self.principio_palabra = nuevo_comienzo
                self.fin_palabra = text.index(INSERT)
                self.linea = text.get(self.principio_palabra, self.fin_palabra)
        else:
            if str(text.index(INSERT)) != "2.1":
                print text.index(INSERT)
                indice_texto = text.index(INSERT)
                lista = indice_texto.split('.')
                lista[1] = str(int(lista[1]) - 1)
                indice_texto = lista[0] + '.' + lista[1]
                text.delete(indice_texto, INSERT)

    def traer_caracter(self, boton):
        for tupla in self.diccionario_letras.items():
            if tupla[0] == boton:
                return tupla[1][self.seleccion_letra]

    def analis_text(self, clave_boton):
        if self.nueva_palabra_incompleta != True:
                if self.linea == '':
                    self.principio_palabra = texto_1.index(INSERT)
                    self.start_to_write_new_word(clave_boton)
                    self.linea = self.diccionario_letras[clave_boton][0]
                else:
                    self.letra = self.diccionario_letras[clave_boton][0]
                    self.linea = self.linea + self.letra
                    self.continue_write_word(self.linea)
                    self.fin_palabra = texto_1.index(INSERT)

        else:
            self.escribir_palabra_nueva(clave_boton)
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
            try:
                if gestor_de_escritura.nueva_palabra_incompleta == False:
                    gestor_de_escritura.borrar(texto_1)
                else:
                    gestor_de_escritura.borrar(texto_2)
            except:
                pass
        if comando == "ok":
            if gestor_de_escritura.sin_opciones == True:
                if self.flag_ok == False:
                    self.flag_ok = True
                    gestor_de_escritura.agregar_palabra()
                else:
                    gestor_de_escritura.terminar_de_agregar_palabra()
                    self.flag_ok = False
            pass
        if comando == '#':
            gestor_de_escritura.espacio()
        if comando == "right":
            if gestor_de_escritura.nueva_palabra_incompleta:
                gestor_de_escritura.anterior_boton = ''
        if comando == "left":
            pass
        if comando == "down":
            gestor_de_escritura.seleccion =\
                                        (gestor_de_escritura.seleccion + 1)\
                                     % len(gestor_de_escritura.mis_opciones)
            gestor_de_escritura.cambiar_opcion()
        if comando == "up":
            gestor_de_escritura.seleccion =\
                                    (gestor_de_escritura.seleccion - 1)\
                                     % len(gestor_de_escritura.mis_opciones)
            gestor_de_escritura.cambiar_opcion()

    def __init__(self):
        self.flag_ok = False
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
