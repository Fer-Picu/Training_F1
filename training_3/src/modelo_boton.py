'''
Created on 26/03/2013

@author: fernando
'''


from Tkinter import *

root = Tk()
class Modelo_Boton(Button):

    def accion_boton(self):
        print id

    def __init__(self, id):
        self.id = id
        Button.__init__(self, root, command = self.accion_boton())
    if __name__ == "__main__":
        __init__()