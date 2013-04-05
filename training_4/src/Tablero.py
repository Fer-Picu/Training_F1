'''
Created on 05/04/2013

@author: fernando
'''


class Tablero():
    '''
    classdocs
    '''

    def make_lista_celdas(self):
        for x in self.rango:
            for y in self.rango:
                self.__lista_celdas.append([x, y])

    def get_lista_celdas(self):
        return self.lista_celdas

    def validar_en_el_campo(self, intento_de_marcaje):
        if intento_de_marcaje in self.__lista_celdas:
            return True

    def validar_disponibilidad(self, celda):
        if celda in self.lista_celdas_marcadas:
            return [celda, False]
        else:
            return [celda, True]
        pass

    def consulta_celda(self, clave):
        auxiliar = self.validar_disponibilidad(clave)
        if self.validar_en_el_campo(clave) and auxiliar[1]:
            return True
        else:
            return False
    def marcar_celda(self):
        pass
    def get_celda(self, n):
        return self.__lista_celdas[n]

    def __init__(self):
        '''
        Constructor
        '''
        self.rango = range(8)
        self.campo = []
        self.lista_celdas_marcadas = []
        self.__lista_celdas = []
        self.make_lista_celdas()
