'''
Created on 05/04/2013

@author: fernando
'''

from Jugador import Jugador


def main():
    chaboncito = Jugador()
    chaboncito.jugar()
    print chaboncito.pony.posicion
    i = 0
    while i < len(chaboncito.machetes_lista):
        for x in chaboncito.machetes_lista[i].lista_de_accesos:
            if x == [7, 7]:
                print 'esta celda: ', chaboncito.machetes_lista[i].id
        i += 1
if __name__ == '__main__':
    main()
