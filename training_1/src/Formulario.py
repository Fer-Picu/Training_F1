'''
Created on 21/03/2013

@author: fernando
'''


class Formulario ():
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.tipo_de_tramite = ''
        self.dni = 0
        self.genero = ''
        pass

    def peticion_de_datos(self):
        while 1:
            self.tipo_de_tramite = raw_input('ingrese tramite CUIL o CUIT: ')
            self.tipo_de_tramite = self.tipo_de_tramite.lower()
            if self.tipo_de_tramite == 'cuil' or 'cuit':
                break
            print 'ingreso incorrecto'
        while 1:
            self.genero = raw_input('HOMBRE: H\MUJER: M\n EMPRESA: E')
            self.genero = self.genero.lower()
            if self.genero[0] == 'h' or 'm' or 'e':
                break
            print 'ingreso incorrecto'
        while 1:
            self.dni = raw_input('ingrese dni')
            if len(self.dni) == 8:
                break
            print 'ingreso incorrecto'
        print self.dni 