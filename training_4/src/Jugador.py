'''
Created on 05/04/2013

@author: fernando
'''


from Tablero import Tablero
from Caballo import Caballo



class Jugador(object):
    '''
    classdocs
    '''
    def get_mapa(self):
        return self.diccionario.items()
    def get_jugadas(self):
        return self.jugadas_alcanzadas

    def calcular_movimientos(self):
        i = 0
        while i < len(self.tablerito._lista_celdas):
            self.pony.set_posicion(self.tablerito._lista_celdas[i][:])
            h = 1
            lista_aux = []
            while h < 9:
                if self.pony.mover(h) == 0:
                    pass
                else:
                    lista_aux.append(self.pony.get_posicion()[:])
                    self.pony.set_posicion(self.tablerito._lista_celdas[i][:])
                h += 1
            self.diccionario[i] = lista_aux[:]
            print 'posibilidades desde : ', self.tablerito._lista_celdas[i][:], '= ', self.diccionario[i]
            i += 1
    def __init__(self):
        '''
        Constructor
        '''
        self.jugadas_alcanzadas = 0
        self.pony = Caballo([0, 0])
        self.tablerito = Tablero()
        self.diccionario = {}