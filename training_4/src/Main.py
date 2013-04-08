'''
Created on 05/04/2013

@author: fernando
'''

from Jugador import Jugador


def main():
    chaboncito = Jugador()
    chaboncito.calcular_movimientos()
    for cada_clave in chaboncito.diccionario.iteritems():
        print 'casillero: ',cada_clave[0], 'posibles = ', cada_clave[1] 
if __name__ == '__main__':
    main()
