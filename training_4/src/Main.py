'''
Created on 05/04/2013

@author: fernando
'''

from Jugador import Jugador


def main():
    chaboncito = Jugador()
    init = int(raw_input('set_posicion_celda: '))
    clave_init = chaboncito.pasar_de_celda_a_clave(init)
    chaboncito.pony.set_posicion(clave_init[:])
    repetida = False
    while chaboncito.get_jugadas() <= 64 and not repetida:
        print 'jugada: ', chaboncito.get_jugadas()
        pre = chaboncito.get_jugadas()
        chaboncito.jugar()
        print 'Posicion: ', chaboncito.pony.get_posicion()
        pro = chaboncito.get_jugadas()
        if pre == pro:
            repetida = True
        print repetida

    print 'ultima_posicion', chaboncito.pony.posicion
if __name__ == '__main__':
    main()
