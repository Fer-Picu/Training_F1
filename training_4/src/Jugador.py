'''
Created on 05/04/2013

@author: fernando
'''


class Jugador(object):
    '''
    classdocs
    '''
    def get_jugadas(self):
        return self.jugadas_alcanzadas

    def __init__(self):
        '''
        Constructor
        '''
        self.jugadas_alcanzadas = 0
