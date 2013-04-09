'''
Created on 05/04/2013

@author: fernando
'''


from Tablero import Tablero
from Caballo import Caballo
from Machete_Celda import Machete_Celda
from sys import exit


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
            self.mapa_diccionario[i] = lista_aux[:]
            i += 1

    def len_opciones(self, clave_celda):
        celda = self.pasar_de_clave_a_celda(clave_celda)
        cantidad = len(self.machetes_lista[celda].lista_de_accesos[:])
        return cantidad

    def terminar(self):
        print 'JUEGO TERMINADO.. juagadas: ', self.contador_jugadas
        exit()

    def jugar(self):
        celda = self.pasar_de_clave_a_celda(self.pony.get_posicion())
        print celda
        opciones_list = self.machetes_lista[celda].lista_de_accesos[:]
        print 'posibilitis desde: ', celda, '= ', opciones_list
        if opciones_list == []:
            self.terminar()
        lista_analisis = []
        for opcion in opciones_list:
            print opcion

    def pasar_de_clave_a_celda(self, clave):
        celda = clave[1] * 8 + clave[0]
        return celda

    def crear_lista_de_machetes(self):
        i = 0
        while i < 64:
            self.machete_aux = Machete_Celda()
            self.machete_aux.set_id(i)
            self.machete_aux.set_accesos_restantes(self.mapa_diccionario[i])
            self.machetes_lista.append(self.machete_aux)
            i += 1

    def pasar_de_celda_a_clave(self, celda):
        ls = [celda % 8, celda / 8]
        return ls[:]

    def quitar_celda_del_mapa(self, celda):
#         PARA LAS OPCIONES QUE TENIAN A CELDA COMO OPCION
        self.machetes_lista[celda].marcar()
        clave_celda_erase = self.pasar_de_celda_a_clave(celda)
        i = 0
        len_accesos_celda_a_borrar = \
            len(self.machetes_lista[celda].lista_de_accesos)
        while i < len_accesos_celda_a_borrar:
            clave_opcion = self.machetes_lista[celda].lista_de_accesos[i]
            celda_opcion = self.pasar_de_clave_a_celda(clave_opcion)
            self.machetes_lista[celda_opcion].
#             j = 0
#             while j < len(self.machetes_lista[celda_opcion].lista_de_accesos):
#                 list_aux =\
#                     self.machetes_lista[celda_opcion].lista_de_accesos[:]
#                 if list_aux[j] == self.pasar_de_celda_a_clave(celda):
#                     self.machetes_lista[celda_opcion].lista_de_accesos[j:j + 1]\
#                                                                        = []
#                 print 'borrado:', celda ,'item: ',celda_opcion,' opciones',self.machetes_lista[celda_opcion].lista_de_accesos
#                 j += 1
            i += 1

    def __init__(self):
        '''
        Constructor
        '''
        self.contador_jugadas = 1
        self.pony = Caballo([0, 0])
        self.tablerito = Tablero()
        self.mapa_diccionario = {}
        self.machete_aux = Machete_Celda()
        self.machetes_lista = []
        self.calcular_movimientos()
        self.crear_lista_de_machetes()
        self.quitar_celda_del_mapa(63)
        self.quitar_celda_del_mapa(46)
        self.quitar_celda_del_mapa(53)
