'''
Created on 05/04/2013

@author: fernando
'''


class Caballo(object):
    '''
    classdocs:
             - El caballo sabe moverse, sabe iniciarse y devolver la posicion
             - Pensado para que las coordenadas los valores mas chicos son en 
                la parte superior izquierda del tablero
    '''
    def validar_movimiento(self, pos_aux):
        variable = 'nok'
        if pos_aux[0] >= 0:
            if pos_aux[0] <= 7:
                if pos_aux[1] > -1:
                    if pos_aux[1] < 8:
                        variable = 'ok'
        return variable

    def set_posicion(self, pos_aux):
        if self.validar_movimiento(pos_aux) == 'nok':
            print 'error de seteo de posicion caballeristica'

    def get_posicion(self):
        return self.posicion[:]

    def disminuir_x_en_2(self):
        self.posicion[0] -= 2

    def disminuir_x_en_1(self):
        self.posicion[0] -= 1

    def disminuir_y_en_2(self):
        self.posicion[1] -= 2

    def disminuir_y_en_1(self):
        self.posicion[1] -= 1

    def aumentar_x_en_2(self):
        self.posicion[0] += 2

    def aumentar_x_en_1(self):
        self.posicion[0] += 1

    def aumentar_y_en_2(self):
        self.posicion[1] += 2

    def aumentar_y_en_1(self):
        self.posicion[1] += 1

    def mover(self, movimiento):
        self.posicion_anterior = self.get_posicion()
        if movimiento == 1:
            self.disminuir_y_en_2()
            self.aumentar_x_en_1()
        elif movimiento == 2:
            self.aumentar_x_en_2()
            self.disminuir_y_en_1()
        elif movimiento == 3:
            self.aumentar_x_en_2()
            self.aumentar_y_en_1()
        elif movimiento == 4:
            self.aumentar_y_en_2()
            self.aumentar_x_en_1()
        elif movimiento == 5:
            self.aumentar_y_en_2()
            self.disminuir_x_en_1()
        elif movimiento == 6:
            self.disminuir_x_en_2()
            self.aumentar_y_en_1()
        elif movimiento == 7:
            self.disminuir_x_en_2()
            self.disminuir_y_en_1()
        elif movimiento == 8:
            self.disminuir_y_en_2()
            self.disminuir_x_en_1()
        if self.validar_movimiento(self.posicion) == 'nok':
            return 0
        else:
            return 1

    def volver_atras(self):
        self.posicion = self.posicion_anterior[:]

    def __init__(self, posicion):
        '''
        Constructor
        '''
        self.posicion = posicion
        self.posicion_anterior = posicion
