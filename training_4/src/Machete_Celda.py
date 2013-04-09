'''
Created on 09/04/2013

@author: fernando
'''

class Machete_Celda(object):
    '''
    classdocs
    '''
    def marcar(self):
        self.marcada = True

    def bajar_cantidad_de_accesos(self, celda_clave):
        i = 0
        while i < len(self.lista_de_accesos):
            if self.lista_de_accesos[i] == celda_clave:
                self.lista_de_accesos[i: (i + 1)] = []
                self.accesos_restantes -= 1
            i += 1
        pass

    def set_id(self, id):
        self.id = id

    def set_accesos_restantes(self, accesos_restantes):
        self.accesos_restantes = len(accesos_restantes)
        self.lista_de_accesos = accesos_restantes[:]

    def __init__(self,):
        '''
        Constructor
        '''
        self.lista_de_accesos = []
        self.accesos_restantes = 0
        self.id = id
        self.marcada = False
