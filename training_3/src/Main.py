'''
Created on 26/03/2013

@author: fernando
'''
import Tkinter
import tkMessageBox
i = 0


class Modelo_Boton():
    def __init__(self,nombre):
        self.i = 0
        self.nombre = nombre
    def accion_boton(self):
        self.i = self.i + 1
        print self.i
        
        
modelo_boton_1 = Modelo_Boton('boton_1')

diccionario_letras = {'2':'a', '22':'b', '222':'c',\
                      '3':'d', '33':'e', '333':'f',\
                      '4':'g', '44':'h', '444':'i',\
                      '5':'j', '55':'k', '555':'l',\
                      '6':'m', '66':'n', '666':'o',\
                      '7':'p', '77':'q', '777':'r', '7777':'s',\
                      '8':'t', '88':'u', '888':'v',\
                      '9':'w', '99':'x', '999':'y', '9999':'z'\
                      }


if __name__ == '__main__':  
    top = Tkinter.Tk()
    boton_1 = Tkinter.Button(top, text ="Hello", command = modelo_boton_1.accion_boton_1)
    boton_1.pack()
    top.mainloop()
