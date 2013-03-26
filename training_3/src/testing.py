'''
Created on 26/03/2013

@author: fernando
'''
import unittest
from Tkinter import *
import tkMessageBox

class Test(unittest.TestCase):


    def testName(self):
        pass



def funcion():
    tkMessageBox.showinfo( "Hello Python", "Hello World")
    i = i + 1
    print i
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    i = 0
   
    root = Tk()
    # 
    # app = App(root)
    frame =  Frame(root)
    frame.pack()
    
    boton = Button(frame, text= 'boton', COMMAND = funcion())
    boton.pack(side= LEFT)
    etiqueta = Label(root, text="Codigo Python")
    etiqueta.pack()
    root.mainloop()