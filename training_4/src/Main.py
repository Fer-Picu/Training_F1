'''
Created on 05/04/2013

@author: fernando
'''

from Jugador import Jugador


def main():
    chaboncito = Jugador()
    init = int(raw_input('set_posicion_celda: '))
    while init < 0 or init > 63:
        print 'ERROR set entre 0 y 63 '
        init = int(raw_input('set_posicion_celda: '))
    clave_init = chaboncito.pasar_de_celda_a_clave(init)
    print clave_init
    chaboncito.pony.posicion = clave_init[:]
    ok = True
    while chaboncito.get_jugadas() <= 64 and ok:
        print 'jugada: ', chaboncito.get_jugadas()
        pre = chaboncito.pony.get_posicion()
        chaboncito.jugar()
        print '********************************=========>>>>>>>>>Posicion: ', chaboncito.pony.get_posicion()
        pro = chaboncito.pony.get_posicion()
        if pre == pro:
            ok = False
            break

    if ok == False:
        print 'mismo lugar se termino jugadas: ', chaboncito.get_jugadas()

if __name__ == '__main__':
    main()
