'''
Created on 05/04/2013

@author: fernando
'''

from Tablero import Tablero
from Caballo import Caballo


def main():
    pony = Caballo([0, 0])
    tablerito = Tablero()
#     i = 0
#     while i < len(tablerito.get_lista_celdas()):
#         print 'celda: ', i, '= ', tablerito.lista_celdas[i]
#         i += 1
    if pony.mover(4) == 0:
        print 'ERROR EL CABALLO NO SABE SUICIDARSE'
    else:
        print 'movimiento correcto'
    if tablerito.marcar_celda(pony.get_posicion()):
        print 'ok'
    else:
        print 'error'
    print tablerito.lista_celdas_marcadas
if __name__ == '__main__':
    main()
