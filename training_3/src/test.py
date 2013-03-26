'''
Created on 26/03/2013

@author: fernando
'''
 
# class App:
# 
#     def __init__(self, master):
# 
#         frame = Frame(master)
#         frame.pack()
# 
#         self.uno = Button(frame, text="1", fg="red", command=self.evento('uno'))
#         self.uno.pack(side=LEFT)
# 
#         self.dos = Button(frame, text="2", command=self.evento('dos'))
#         self.dos.pack(side=LEFT)    
# 
#         self.tres = Button(frame, text="3", command=self.evento('tres'))
#         self.tres.pack(side=LEFT)
#         
#         self.cuatro = Button(frame, text="4", command=self.evento('cuatro'))
#         self.cuatro.pack(side=LEFT)
#         
#         self.cinco = Button(frame, text="5", command=self.evento('cinco'))
#         self.cinco.pack(side=LEFT)
#         
#         self.seis = Button(frame, text="6", command=self.evento('seis'))
#         self.seis.pack(side=LEFT)
#         
#         self.siete = Button(frame, text="7", command=self.evento('siete'))
#         self.siete.pack(side=LEFT)
#         
#         self.ocho = Button(frame, text="8", command=self.evento('ocho'))
#         self.ocho.pack(side=LEFT)
#         
#         self.nueve = Button(frame, text="9", command=self.evento('nueve'))
#         self.nueve.pack(side=LEFT)
# 
#     def evento(self, identificacion):
#         print identificacion
#         
#     
# 
# 
# app = App(root)

from Tkinter import *
import tkMessageBox

def funcion():
    tkMessageBox.showinfo( "Hello Python", "Hello World")
    i = i + 1
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
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


# import Tkinter
# import tkMessageBox
# 
# top = Tkinter.Tk()
# 
# def helloCallBack():
#     tkMessageBox.showinfo( "Hello Python", "Hello World")
# 
# B = Tkinter.Button(top, text ="Hello", command = helloCallBack)
# 
# B.pack()
# top.mainloop()