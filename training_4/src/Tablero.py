'''
Created on 05/04/2013

@author: fernando
'''


class Tablero():
    '''
    classdocs
    '''

    def make_lista_celdas(self):
        y = 0
        while y < 8:
            x = 0
            while x < 8:
                self._lista_celdas.append([x, y])
                x += 1
            y += 1

    def get_lista_celdas(self):
        return self.lista_celdas

    def validar_en_el_campo(self, intento_de_marcaje):
        if intento_de_marcaje in self._lista_celdas:
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

#     def marcar_celda(self, celda):
#         for alguna_celda  in self._lista_celdas:
#             if alguna_celda == celda:
#                 self.lista_celdas_marcadas.append(celda)

    def get_celda(self, n):
        return self._lista_celdas[n]

    def __init__(self):
        '''
        Constructor
        '''
        self.rango = range(8)
        self.campo = []
        self.lista_celdas_marcadas = [[2, 1]]
        self._lista_celdas = []
        self.make_lista_celdas()
